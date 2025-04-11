#!/usr/bin/env python
import difflib
from pathlib import Path


# could maybe parallelise this by combining blocks?

def main():
    a_fp = Path("dialogue-process/done.txt")
    b_fp = Path("lyrics-process/done.txt")
    a = a_fp.read_text()
    b = b_fp.read_text()

    matcher = difflib.SequenceMatcher(a=a, b=b)
    print(matcher.get_matching_blocks())


if __name__ == "__main__":
    main()
