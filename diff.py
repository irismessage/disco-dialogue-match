#!/usr/bin/env python
import logging
from concurrent.futures import ProcessPoolExecutor
from difflib import Match, SequenceMatcher
from pathlib import Path
from sys import stderr
from typing import Sequence

import tokenise

# the problem with the difflib algorithm:
# > difflib.SequenceMatcher(a='abc def', b='def abc').get_matching_blocks()
# [Match(a=0, b=4, size=3), Match(a=7, b=7, size=0)]
# e.g. both texts contain "feel like a traveller"
# but cause of the ordering this doesn't catch it
TEST = False

log = logging.getLogger()
logging.basicConfig(level=logging.INFO, stream=stderr)


def difflib_match(a: Sequence, b: Sequence) -> list[Match]:
    matcher = SequenceMatcher(a=a, b=b, autojunk=False)
    return matcher.get_matching_blocks()


def my_match(a: Sequence, b: Sequence) -> list[Match]:
    def match_b(cursor_a: int) -> list[Match]:
        log.info(cursor_a / len(a))
        matches = []

        for cursor_b in range(len(b)):
            if a[cursor_a] == b[cursor_b]:
                match_size = 1
                while (
                    cursor_a + match_size < len(a)
                    and cursor_b + match_size < len(b)
                    and a[cursor_a + match_size] == b[cursor_b + match_size]
                ):
                    match_size += 1

                matches.append(Match(cursor_a, cursor_b, match_size))

        return matches

    matches = []
    with ProcessPoolExecutor() as executor:
        for matches_b in executor.map(match_b, range(len(a))):
            matches.extend(matches_b)

    return matches


def main():
    log.info("start")
    if TEST:
        fp_dialogue = Path("testa.txt")
        fp_lyrics = Path("testb.txt")
    else:
        fp_dialogue = Path("dialogue-process/done.txt")
        fp_lyrics = Path("lyrics-process/done.txt")

    token_dialogue = tokenise.tokenise(fp_dialogue.read_text())
    token_lyrics = tokenise.tokenise(fp_lyrics.read_text())
    log.info("tokenised")

    matches = my_match(token_dialogue, token_lyrics)
    log.info("matched")
    matches.sort(key=lambda m: m.size, reverse=True)
    log.info("sorted")

    print(
        "\n".join(
            tokenise.detokenise(token_lyrics[m.b : m.b + m.size]) for m in matches
        )
    )


if __name__ == "__main__":
    main()
