#!/usr/bin/env python3
"""Report the stream properties of the puzzle videos.

This exists so the resolution claim is checkable rather than asserted. The
catalogue entry this folder replaces stated that only a 360p rendition is
served, and concluded from that the puzzle is blocked on obtaining a better
source. Every copy measured here is 1280x720 at 60 fps.

The videos are not stored in this repository. Fetch them first, for example
with yt-dlp, then point this script at the directory holding them.

Usage:
    python3 tools/probe_videos.py <directory of .mp4 or .webm files>
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

FIELDS = "stream=codec_name,width,height,r_frame_rate,nb_frames"


def probe(path: Path) -> dict | None:
    try:
        out = subprocess.run(
            ["ffprobe", "-v", "error", "-select_streams", "v:0",
             "-show_entries", FIELDS, "-of", "json", str(path)],
            capture_output=True, text=True, check=True).stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    streams = json.loads(out).get("streams") or []
    return streams[0] if streams else None


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    directory = Path(sys.argv[1])
    files = sorted(p for p in directory.iterdir()
                   if p.suffix in {".mp4", ".webm", ".mkv"})
    if not files:
        print(f"no video files in {directory}")
        return 1

    print(f"{'file':38s} {'codec':6s} {'size':11s} {'fps':7s} frames")
    for path in files:
        info = probe(path)
        if info is None:
            print(f"{path.name:38s} could not probe (is ffprobe installed?)")
            continue
        size = f"{info.get('width')}x{info.get('height')}"
        print(f"{path.name:38s} {info.get('codec_name',''):6s} {size:11s} "
              f"{info.get('r_frame_rate',''):7s} {info.get('nb_frames','')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
