#!/usr/bin/env python3
"""Mirror every recovered artifact, then hash it repeatedly, checking each depth.

Motivation. The puzzle displays the word MIRROR on screen, and it demonstrates a
bit mirror in its own C8-to-19 instruction, so mirroring is the setter's own
operation rather than an imported guess. Eight is likewise available from the
puzzle: the payload is eight bytes, and C8 carries an eight.

Two gaps this closes. Earlier work iterated SHA-256 to seven rounds and stopped,
so a depth of eight was never reached. And mirroring and iterated hashing were
tested separately, never composed.

Every intermediate depth is checked, not only the depth of interest, so a result
at any round count would be caught.

Usage:
    python3 tools/test_mirror_iterated_hash.py [max_depth]
"""
from __future__ import annotations

import hashlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from oracle import eth_address, TARGET  # noqa: E402

try:
    from Crypto.Hash import keccak
except ImportError:
    keccak = None

READING = "6A6B0860B4723504"
PART1, PART2 = "6A6B0860B4", "723504"
PUZZLE1_KEY = "4487FC620AD0C4C67E80BE342B2EA1F5A3DC482BE6FB9C2451007322EA8BE35F"
TITLE = "CRYPTO PUZZLERPART 1MIRRORPART 2"
ORDER = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141


def bit_mirror_byte(data: bytes) -> bytes:
    return bytes(int(f"{b:08b}"[::-1], 2) for b in data)


def bit_mirror_whole(data: bytes) -> bytes:
    bits = "".join(f"{b:08b}" for b in data)[::-1]
    return bytes(int(bits[i:i + 8], 2) for i in range(0, len(bits), 8))


def nibble_swap(data: bytes) -> bytes:
    return bytes(((b & 0x0F) << 4) | (b >> 4) for b in data)


def seeds() -> dict[str, bytes]:
    out: dict[str, bytes] = {}
    for name, text in (("reading", READING), ("part1", PART1), ("part2", PART2),
                       ("part2-then-part1", PART2 + PART1), ("title", TITLE)):
        out[f"{name}-ascii"] = text.encode()
        out[f"{name}-ascii-lower"] = text.lower().encode()
    out["reading-hex"] = bytes.fromhex(READING)
    out["part1-hex"] = bytes.fromhex(PART1)
    out["puzzle1-key-hex"] = bytes.fromhex(PUZZLE1_KEY)
    out["c8"] = bytes([0xC8])
    return out


def mirrors(data: bytes) -> dict[str, bytes]:
    text = data.decode("latin-1")
    return {
        "none": data,
        "reverse-bytes": data[::-1],
        "reverse-text": text[::-1].encode("latin-1"),
        "bit-mirror-per-byte": bit_mirror_byte(data),
        "bit-mirror-whole": bit_mirror_whole(data),
        "nibble-swap": nibble_swap(data),
        "bit-mirror-then-reverse": bit_mirror_byte(data)[::-1],
    }


def hashers():
    out = {
        "sha256": lambda b: hashlib.sha256(b).digest(),
        "sha3-256": lambda b: hashlib.sha3_256(b).digest(),
        "blake2s": lambda b: hashlib.blake2s(b).digest(),
        "sha512-first32": lambda b: hashlib.sha512(b).digest()[:32],
    }
    if keccak is not None:
        out["keccak256"] = lambda b: keccak.new(digest_bits=256, data=b).digest()
    return out


def main() -> None:
    max_depth = int(sys.argv[1]) if len(sys.argv) > 1 else 16
    target = TARGET.lower()
    tested = 0
    hits = []

    for seed_name, seed in seeds().items():
        for mirror_name, mirrored in mirrors(seed).items():
            for hash_name, digest in hashers().items():
                current = mirrored
                for depth in range(1, max_depth + 1):
                    current = digest(current)
                    tested += 1
                    value = int.from_bytes(current, "big")
                    if not 0 < value < ORDER:
                        continue
                    if eth_address(current.hex()).lower() == target:
                        hits.append((seed_name, mirror_name, hash_name, depth,
                                     current.hex()))

    print(f"seeds {len(seeds())}  mirrors 7  hashes {len(hashers())}  "
          f"depths 1..{max_depth}")
    print(f"candidates tested: {tested}")
    for hit in hits:
        print("MATCH", hit)
    if not hits:
        print("0 match")


if __name__ == "__main__":
    main()
