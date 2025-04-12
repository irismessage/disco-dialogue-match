#!/usr/bin/env python
import difflib
from difflib import Match
from pathlib import Path

import tokenise


# could maybe parallelise this by combining blocks?
def print_matching_blocks(a, b):
    matcher = difflib.SequenceMatcher(a=a, b=b)
    print(matcher.get_matching_blocks())


def load_matching_blocks() -> list[Match]:
    fp = Path("matches.txt")
    matches = eval(fp.read_text())
    return matches


def main():
    fp_dialogue = Path("dialogue-process/done.txt")
    fp_lyrics = Path("lyrics-process/done.txt")

    token_dialogue = tokenise.tokenise(fp_dialogue.read_text())
    token_lyrics = tokenise.tokenise(fp_lyrics.read_text())

    matcher = difflib.SequenceMatcher(a=token_dialogue, b=token_lyrics, autojunk=False)
    matches = matcher.get_matching_blocks()

    print(
        "\n".join(
            tokenise.detokenise(token_lyrics[m.b : m.b + m.size]) for m in matches
        )
    )


if __name__ == "__main__":
    main()
