"""Fast batch oracle: does any candidate 32-byte key hash to the LVL5 target address?

Compares hash160 directly rather than base58-encoding, and uses coincurve (libsecp256k1)
rather than pure-python ecdsa -- roughly 33k keys/sec per core.
"""

import hashlib
from multiprocessing import Pool

import base58
from coincurve import PrivateKey

TARGET = "1cryptoGeCRiTzVgxBQcKFFjSVydN1GW7"
# Zden's puzzle addresses are uncompressed (verified against his published LVL3 key),
# but we check both forms since it costs one extra hash.
TARGET_HASH160 = base58.b58decode_check(TARGET)[1:]

SECP256K1_ORDER = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141


def matches(priv: bytes, target: bytes = TARGET_HASH160) -> str | None:
    """Return which pubkey form matched the target hash160, or None."""
    value = int.from_bytes(priv, "big")
    if not 0 < value < SECP256K1_ORDER:
        return None
    pub = PrivateKey(priv).public_key
    for label, compressed in (("uncompressed", False), ("compressed", True)):
        blob = pub.format(compressed=compressed)
        h = hashlib.new("ripemd160", hashlib.sha256(blob).digest()).digest()
        if h == target:
            return label
    return None


# The target travels with each chunk. Module-level state does NOT propagate to workers
# under macOS spawn semantics, so passing it explicitly is what makes the harness
# testable against a known-answer control.
def _worker(payload):
    target, chunk = payload
    return [(p, m) for p in chunk if (m := matches(p, target))]


def scan(keys, target: bytes = TARGET_HASH160, processes: int = 8, chunk: int = 20000):
    """Scan an iterable of 32-byte keys. Returns [(key, form), ...] for any matches."""
    keys = list(keys)
    chunks = [(target, keys[i : i + chunk]) for i in range(0, len(keys), chunk)]
    found = []
    with Pool(processes) as pool:
        for result in pool.imap_unordered(_worker, chunks):
            found.extend(result)
    return found


if __name__ == "__main__":
    # Self-test: LVL3's published key must match LVL3's address under the same machinery.
    lvl3_priv = bytes.fromhex(
        "6008C37D0AA226DBBE611BE64106964BCA6CBBA7098FE4602A932C590E14B074"
    )
    lvl3_hash = base58.b58decode_check("1cryptoJzomVVJUSys8Qv1gKPCXFoZy1U")[1:]
    pub = PrivateKey(lvl3_priv).public_key.format(compressed=False)
    got = hashlib.new("ripemd160", hashlib.sha256(pub).digest()).digest()
    print("self-test:", "PASS" if got == lvl3_hash else "FAIL")
    print("target hash160:", TARGET_HASH160.hex())
