"""HALV-specific address oracle, with a positive control.

WHY THIS EXISTS: the LVL5 oracle module defaults its target to the LVL5 address. Importing
`matches` from it and calling matches(key) silently checks the wrong puzzle. Both addresses
are "1crypto" vanity addresses so their hash160s share the prefix 06c84797, which makes the
mistake invisible on a glance:

    LVL5 1cryptoGeCRiTzVgxBQcKFFjSVydN1GW7 -> 06c84797d2441393513e2169338e00cf2e755c8c
    HALV 1crypto24HCr178iMcKd5iUi5D4rsg1nK -> 06c84797d1f468b9d5773a61c80073b344df7470

Always import `matches` from THIS module for HALV work, and run the self-test first.
"""

import hashlib

import base58
from coincurve import PrivateKey

TARGET = "1crypto24HCr178iMcKd5iUi5D4rsg1nK"
TARGET_H160 = base58.b58decode_check(TARGET)[1:]
ORDER = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141


def matches(priv: bytes, target: bytes = TARGET_H160):
    """Return which pubkey form hits the target hash160, or None."""
    v = int.from_bytes(priv, "big")
    if not 0 < v < ORDER:
        return None
    pub = PrivateKey(priv).public_key
    for label, comp in (("uncompressed", False), ("compressed", True)):
        blob = pub.format(compressed=comp)
        if hashlib.new("ripemd160", hashlib.sha256(blob).digest()).digest() == target:
            return label
    return None


def self_test():
    """Positive control: a key we own must be found, and the LVL5 target must NOT match."""
    priv = hashlib.sha256(b"halv-oracle-selftest").digest()
    pub = PrivateKey(priv).public_key.format(compressed=False)
    h160 = hashlib.new("ripemd160", hashlib.sha256(pub).digest()).digest()
    ok_pos = matches(priv, h160) == "uncompressed"

    lvl5 = base58.b58decode_check("1cryptoGeCRiTzVgxBQcKFFjSVydN1GW7")[1:]
    ok_neg = TARGET_H160 != lvl5

    print(f"  positive control: {'PASS' if ok_pos else 'FAIL'}")
    print(f"  target is HALV, not LVL5: {'PASS' if ok_neg else 'FAIL'}")
    print(f"  HALV hash160: {TARGET_H160.hex()}")
    return ok_pos and ok_neg


if __name__ == "__main__":
    print("halv_oracle self-test:")
    print("OK" if self_test() else "BROKEN")


# --- parallel batch scanning ---------------------------------------------------------
from multiprocessing import Pool  # noqa: E402


def _worker(payload):
    target, chunk = payload
    return [(k, m) for k in chunk if (m := matches(k, target))]


def scan(keys, target: bytes = TARGET_H160, processes: int = 8, chunk: int = 20000):
    """Scan an iterable of 32-byte keys in parallel. Returns [(key, form), ...]."""
    keys = list(keys)
    chunks = [(target, keys[i:i + chunk]) for i in range(0, len(keys), chunk)]
    found = []
    with Pool(processes) as pool:
        for res in pool.imap_unordered(_worker, chunks):
            found.extend(res)
    return found
