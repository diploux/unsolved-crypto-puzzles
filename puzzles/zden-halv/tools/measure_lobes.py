#!/usr/bin/env python3
"""Count the waveform's lobes and its distinct peak amplitudes.

This script exists to make one number checkable. The catalogue this repository
replaces stated that the waveform has 59 lobes, "reproduced identically across 3
independent measurement passes", and that amplitude is decorative, halving every
8 lobes. From the 59 figure it derived an information capacity of about 118 bits
against the 256 a private key needs, and recommended abandoning pixel-level work
on the image. No producing script was published for the 59 figure.

This script reports 63 lobes and 17 distinct positive peak amplitudes.

Input and its provenance
------------------------
The input is the extracted 8x32 level matrix, not the raw pixels. Extraction is
a separate step with its own verification: the sample lattice is 256 positions
at 3 px, centres at x = 92.5 + 3i, and each position carries one level in
{0,1,2,3} against a per-band amplitude unit that halves across the eight bands
(128, 64, 32, 16, 8, 4, 2, 1). Two independent fitting objectives agree on all
256 levels, and a full antialiased forward render reproduces them. Counting
lobes from raw columns instead would be wrong: the stroke has width, so a
position at level 0 still leaves about one pixel of ink beside the centreline
and would be miscounted as nonzero.

Definitions, stated so they can be disagreed with precisely:

  lobe            one maximal run of consecutive positions with nonzero
                  physical amplitude
  peak amplitude  the largest physical amplitude within a lobe, in pixels,
                  that is level times the band's unit

Usage:
    python3 tools/measure_lobes.py
"""
from __future__ import annotations

# The verified extraction. Band b, position p holds a level in {0,1,2,3}.
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
BAND_UNITS = (128, 64, 32, 16, 8, 4, 2, 1)


def physical_amplitudes() -> list[int]:
    out: list[int] = []
    for band, row in enumerate(ROWS):
        for char in row:
            out.append(int(char) * BAND_UNITS[band])
    return out


def maximal_nonzero_runs(values: list[int]) -> list[tuple[int, int]]:
    found: list[tuple[int, int]] = []
    index = 0
    while index < len(values):
        if values[index] > 0:
            start = index
            while index < len(values) and values[index] > 0:
                index += 1
            found.append((start, index - 1))
        else:
            index += 1
    return found


def main() -> None:
    amps = physical_amplitudes()
    assert len(amps) == 256, len(amps)

    lobes = maximal_nonzero_runs(amps)
    peaks = [max(amps[start:end + 1]) for start, end in lobes]
    distinct = sorted(set(peaks))

    print(f"sample positions: {len(amps)}")
    print(f"lobes (maximal nonzero runs): {len(lobes)}")
    print(f"distinct positive peak amplitudes: {len(distinct)}")
    print(f"levels: {distinct}")
    print()
    print("The eight band envelope maxima are 384, 192, 96, 48, 24, 12, 6, 3.")
    print("A decorative ladder halving once every 8 lobes would give 8 distinct")
    print(f"peak levels. The measurement gives {len(distinct)}, so peak")
    print("amplitude carries more distinctions than the band ladder alone.")


if __name__ == "__main__":
    main()
