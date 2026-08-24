#!/usr/bin/env python3
"""Refresh the USD snapshot in every puzzle manifest and README.

Prices go stale silently, which is how the catalogue this replaces ended up
quoting BTC at $63,000 months later. This script re-reads live prices, writes
them into each `puzzle.json` prize block, and rewrites the USD line inside the
`<!-- verified-state:start -->` block of each README.

Two independent sources are queried and compared. If they disagree by more than
one percent the script stops rather than picking one, because a bad price that
looks precise is worse than no price.

Usage:
    python3 tools/refresh_prices.py            # show what would change
    python3 tools/refresh_prices.py --write    # apply
"""
from __future__ import annotations

import json
import re
import sys
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUZZLES = ROOT / "puzzles"
TOLERANCE = 0.01

SATS_PER_BTC = 100_000_000


def fetch(url: str) -> dict:
    with urllib.request.urlopen(url, timeout=25) as response:
        return json.loads(response.read().decode())


def live_prices() -> dict[str, float]:
    coingecko = fetch(
        "https://api.coingecko.com/api/v3/simple/price"
        "?ids=bitcoin,ethereum,arweave&vs_currencies=usd"
    )
    mempool = fetch("https://mempool.space/api/v1/prices")

    btc_a = float(coingecko["bitcoin"]["usd"])
    btc_b = float(mempool["USD"])
    drift = abs(btc_a - btc_b) / min(btc_a, btc_b)
    if drift > TOLERANCE:
        raise SystemExit(
            f"BTC sources disagree by {drift:.2%} ({btc_a} vs {btc_b}); "
            "refusing to write a price"
        )
    return {
        "bitcoin": round((btc_a + btc_b) / 2, -2),
        "ethereum": float(coingecko["ethereum"]["usd"]),
        "arweave": float(coingecko["arweave"]["usd"]),
    }


def usd_value(prize: dict, prices: dict[str, float]) -> float | None:
    amount = prize.get("amount")
    asset = (prize.get("asset") or "").lower()
    if amount is None:
        return None
    if asset == "sats":
        return amount / SATS_PER_BTC * prices["bitcoin"]
    if asset == "btc":
        return amount * prices["bitcoin"]
    if asset == "eth":
        return amount * prices["ethereum"]
    if asset == "ar":
        return amount * prices["arweave"]
    if asset in {"usdt", "usdc", "usd"}:
        return float(amount)
    return None


def approx(value: float) -> str:
    if value >= 1000:
        return f"about ${value:,.0f}"
    return f"about ${value:,.0f}"


def main() -> int:
    write = "--write" in sys.argv
    prices = live_prices()
    today = date.today().isoformat()
    print(f"BTC ${prices['bitcoin']:,.0f}  ETH ${prices['ethereum']:,.2f}  "
          f"AR ${prices['arweave']:,.2f}   ({today})\n")

    changed = 0
    for manifest_path in sorted(PUZZLES.glob("*/puzzle.json")):
        manifest = json.loads(manifest_path.read_text())
        prize = manifest.get("prize") or {}
        value = usd_value(prize, prices)
        if value is None:
            continue
        slug = manifest_path.parent.name
        old = prize.get("usd_estimate")
        print(f"{slug}: {old} -> {value:,.0f}")
        changed += 1
        if not write:
            continue

        prize["usd_estimate"] = round(value)
        prize["usd_snapshot"] = today
        manifest["prize"] = prize
        manifest["last_updated"] = today
        manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")

        readme = manifest_path.parent / "README.md"
        if not readme.exists():
            continue
        text = readme.read_text()
        asset = (prize.get("asset") or "").lower()
        unit = "BTC" if asset in {"sats", "btc"} else asset.upper()
        rate = prices["bitcoin"] if unit == "BTC" else (
            prices["ethereum"] if unit == "ETH" else prices["arweave"])
        replacement = (
            f"({approx(value)} at {unit} = ${rate:,.0f}, {today})"
            if unit == "BTC" else
            f"({approx(value)} at {unit} = ${rate:,.2f}, {today})"
        )
        new_text = re.sub(r"\(about \$[^)]*\)", replacement, text, count=1)
        if new_text != text:
            readme.write_text(new_text)

    print(f"\n{changed} manifests {'updated' if write else 'would change'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
