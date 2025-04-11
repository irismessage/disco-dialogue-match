#!/usr/bin/env python
import difflib
from difflib import Match
from pathlib import Path


# could maybe parallelise this by combining blocks?
def print_matching_blocks(a, b):
    matcher = difflib.SequenceMatcher(a=a, b=b)
    print(matcher.get_matching_blocks())


def load_matching_blocks() -> list[Match]:
    fp = Path("matches.txt")
    matches = eval(fp.read_text())
    return matches


def main():
    a_fp = Path("dialogue-process/done.txt")
    b_fp = Path("lyrics-process/done.txt")
    a = a_fp.read_text()
    b = b_fp.read_text()

    # print_matching_blocks(a, b)

    matches = load_matching_blocks()
    for m in matches:
        print(a[m.a:m.a + m.size])


if __name__ == "__main__":
    main()
