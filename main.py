#!/usr/bin/env python3
"""news-image-20261121 entry: emit the front-page image for 21 Nov 2026.

The rendered front page lives in this repository as frontpage.png. This
program copies it, byte for byte, to entry.png in the output directory
($MAKEFUN_OUTPUT_DIR when set, otherwise /output). After copying, it checks
the output is a real PNG of at most 1 MiB and prints the path and size.
Standard library only; two runs produce identical bytes.
"""

import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "frontpage.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, dest)
    size = os.path.getsize(dest)
    if size > 1048576:
        raise ValueError(f"entry.png is {size} bytes, over the 1 MiB limit")
    with open(dest, "rb") as f:
        header = f.read(8)
    if header != b"\x89PNG\r\n\x1a\n":
        raise ValueError("entry.png does not start with the PNG magic bytes")
    print(f"wrote {dest} ({size} bytes)")


if __name__ == "__main__":
    main()
