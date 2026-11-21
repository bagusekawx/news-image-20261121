#!/usr/bin/env python3
"""news-image-20261121 entry: emit the front-page image for 21 Nov 2026.

The rendered front page lives in this repository as frontpage.png. This
program copies it, byte for byte, to entry.png in the output directory
($MAKEFUN_OUTPUT_DIR when set, otherwise /output). Standard library only;
two runs produce identical bytes.
"""

import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "frontpage.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(source, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
