#!/usr/bin/env python3
"""Test AES-128 constructions on the corrected 16-character reading.

Why this exists. Earlier AES work on this puzzle used the superseded
nine-character reading, bit-packed into eight bytes and doubled to make a key.
Two readings were never tried: the corrected sixteen characters, and the
observation that sixteen characters taken as text are exactly sixteen bytes,
which is precisely an AES-128 key.

On "reversing AES": AES cannot be inverted without its key, so there is no sense
in which the recovered characters can be run backwards on their own. The
characters are also only eight bytes once hex-decoded, which is half an AES
block. The meaningful direction is the other one: treat the sixteen characters
as a key and see whether any natural plaintext encrypts, or decrypts, to a
32-byte value that derives the escrow.

Usage:
    python3 tools/test_aes128.py
"""
from __future__ import annotations

import hashlib
import itertools
import sys
from pathlib import Path

from Crypto.Cipher import AES

sys.path.insert(0, str(Path(__file__).resolve().parent))
from oracle import eth_address, TARGET  # noqa: E402

READING = "6A6B0860B4723504"
PART1, PART2 = "6A6B0860B4", "723504"
PUZZLE1_KEY = "4487FC620AD0C4C67E80BE342B2EA1F5A3DC482BE6FB9C2451007322EA8BE35F"


def keys() -> dict[str, bytes]:
    """Sixteen-byte AES-128 keys built from the reading."""
    out: dict[str, bytes] = {}
    text_forms = {
        "ascii": READING,
        "ascii-lower": READING.lower(),
        "ascii-reversed": READING[::-1],
        "ascii-swapped": PART2 + PART1,
        "ascii-p2-first-lower": (PART2 + PART1).lower(),
    }
    for name, text in text_forms.items():
        raw = text.encode()
        if len(raw) == 16:
            out[name] = raw

    eight = bytes.fromhex(READING)
    out["hex-doubled"] = eight * 2
    out["hex-mirrored"] = eight + eight[::-1]
    out["hex-zero-padded"] = eight + b"\x00" * 8
    out["sha256-of-ascii-first16"] = hashlib.sha256(READING.encode()).digest()[:16]
    return out


def plaintexts() -> dict[str, bytes]:
    """Thirty-two byte blocks a setter might plausibly encrypt."""
    out: dict[str, bytes] = {}
    eight = bytes.fromhex(READING)
    out["reading-ascii-doubled"] = (READING * 2).encode()[:32]
    out["reading-hex-repeated"] = (eight * 4)[:32]
    out["zeros"] = b"\x00" * 32
    out["ones"] = b"\xff" * 32
    out["puzzle1-key-hex"] = bytes.fromhex(PUZZLE1_KEY)
    phrase = "CRYPTO PUZZLERPART 1MIRRORPART 2"
    out["title-phrase"] = phrase.encode()
    out["title-phrase-lower"] = phrase.lower().encode()
    for name, value in list(out.items()):
        assert len(value) == 32, (name, len(value))
    return out


def main() -> None:
    target = TARGET.lower()
    tested = 0
    hits = []

    for key_name, key in keys().items():
        for pt_name, block in plaintexts().items():
            for mode_name, produce in (
                ("ecb-encrypt",
                 lambda k, b: AES.new(k, AES.MODE_ECB).encrypt(b)),
                ("ecb-decrypt",
                 lambda k, b: AES.new(k, AES.MODE_ECB).decrypt(b)),
                ("cbc-zero-iv-encrypt",
                 lambda k, b: AES.new(k, AES.MODE_CBC, b"\x00" * 16).encrypt(b)),
                ("cbc-zero-iv-decrypt",
                 lambda k, b: AES.new(k, AES.MODE_CBC, b"\x00" * 16).decrypt(b)),
            ):
                candidate = produce(key, block)
                tested += 1
                value = int.from_bytes(candidate, "big")
                if not 0 < value < 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141:
                    continue
                if eth_address(candidate.hex()).lower() == target:
                    hits.append((key_name, pt_name, mode_name, candidate.hex()))

    print(f"AES-128 candidates tested: {tested}")
    print(f"keys: {len(keys())}  plaintexts: {len(plaintexts())}  modes: 4")
    for hit in hits:
        print("MATCH", hit)
    if not hits:
        print("0 match")


if __name__ == "__main__":
    main()
