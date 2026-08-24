"""Audit the visibly forced 4+4 split of HALV's phase-aligned words.

This is deliberately an evidence script, not a candidate-key search.  It shows why the
middle five bands form an exact hexadecimal alphabet and separates the complementary bits
carried only by the three exceptional bands.
"""
from __future__ import annotations

import numpy as np


ROWS = (
    "21112330030002311012211013210032",
    "22100300232223023302220223123202",
    "30221022002230203020102020020020",
    "00200003020202210200022000220020",
    "02200030221022002200002020102000",
    "03022100220023000200010201022100",
    "00020002002010000002200230221000",
    "02231120023301001113103112130100",
)


def nibble(bits: tuple[int, int, int, int]) -> int:
    return sum(bit << (3 - index) for index, bit in enumerate(bits))


def main() -> None:
    matrix = np.asarray([[int(char) for char in row] for row in ROWS], dtype=np.uint8)
    words = np.asarray([np.roll(matrix[band], band).reshape(8, 4)
                        for band in range(8)])

    data: list[int] = []
    complement: list[int] = []
    for band in range(8):
        for word in words[band]:
            pairs = tuple((int(value) >> 1, int(value) & 1) for value in word)
            data.append(nibble((pairs[0][0], pairs[1][0], pairs[2][0], pairs[2][1])))
            complement.append(nibble((pairs[0][1], pairs[1][1], pairs[3][0], pairs[3][1])))

    print("phase-aligned words by band:")
    for band, row in enumerate(words):
        print(f"  {band}: " + " ".join("".join(map(str, word)) for word in row))

    print("\ndata nibbles:      ", "".join(f"{value:X}" for value in data))
    print("complement nibbles:", "".join(f"{value:X}" for value in complement))
    print("middle complement is zero:", not any(complement[16:56]))
    print("nonzero complement indices:",
          [(index, f"{value:X}") for index, value in enumerate(complement) if value])

    for band in range(2, 7):
        row = words[band]
        capacities = tuple(len(set(map(int, row[:, lane]))) for lane in range(4))
        print(f"band {band} lane cardinalities: {capacities}")


if __name__ == "__main__":
    main()
