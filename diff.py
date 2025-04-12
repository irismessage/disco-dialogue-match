#!/usr/bin/env python
from difflib import Match, SequenceMatcher
from pathlib import Path
from typing import Sequence

import tokenise

# the problem with the difflib algorithm:
# > difflib.SequenceMatcher(a='abc def', b='def abc').get_matching_blocks()
# [Match(a=0, b=4, size=3), Match(a=7, b=7, size=0)]
# e.g. both texts contain "feel like a traveller"
# but cause of the ordering this doesn't catch it
TEST = False


def difflib_match(a: Sequence, b: Sequence) -> list[Match]:
    matcher = SequenceMatcher(a=a, b=b, autojunk=False)
    return matcher.get_matching_blocks()


def my_match(a: Sequence, b: Sequence) -> list[Match]:
    pass


def main():
    if TEST:
        fp_dialogue = Path("testa.txt")
        fp_lyrics = Path("testb.txt")
    else:
        fp_dialogue = Path("dialogue-process/done.txt")
        fp_lyrics = Path("lyrics-process/done.txt")

    token_dialogue = tokenise.tokenise(fp_dialogue.read_text())
    token_lyrics = tokenise.tokenise(fp_lyrics.read_text())

    matches = difflib_match(token_dialogue, token_lyrics)

    print(
        "\n".join(
            tokenise.detokenise(token_lyrics[m.b : m.b + m.size]) for m in matches
        )
    )


if __name__ == "__main__":
    main()
