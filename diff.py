#!/usr/bin/env python
import logging
from concurrent.futures import ProcessPoolExecutor
from difflib import Match, SequenceMatcher
from itertools import repeat, batched
from pathlib import Path
from sys import stderr
from typing import Sequence

import tokenise

# the problem with the difflib algorithm:
# > difflib.SequenceMatcher(a='abc def', b='def abc').get_matching_blocks()
# [Match(a=0, b=4, size=3), Match(a=7, b=7, size=0)]
# e.g. both texts contain "feel like a traveller"
# but cause of the ordering this doesn't catch it
TEST = True
MATCH_LENGTH_THRESHOLD = 2

log = logging.getLogger()
logging.basicConfig(level=logging.INFO, stream=stderr)


def difflib_match(a: Sequence, b: Sequence) -> list[Match]:
    matcher = SequenceMatcher(a=a, b=b, autojunk=False)
    return matcher.get_matching_blocks()


def match_b(range_a: range, a: Sequence, b: Sequence) -> list[Match]:
    milestone_split = len(a) / 10
    milestone = 0

    matches = []
    for cursor_a in range_a:
        if cursor_a > milestone:
            log.info(f"process {range_a.start} {cursor_a / len(a) * 100:.2f}%")
            milestone += milestone_split

        cursor_b = 0
        while cursor_b < len(b):
            if a[cursor_a] == b[cursor_b]:
                match_size = 1
                while (
                    cursor_a + match_size < len(a)
                    and cursor_b + match_size < len(b)
                    and a[cursor_a + match_size] == b[cursor_b + match_size]
                ):
                    match_size += 1

                if match_size > MATCH_LENGTH_THRESHOLD:
                    matches.append(Match(cursor_a, cursor_b, match_size))

                cursor_b += match_size
            else:
                cursor_b += 1

    return matches


def my_match(a: Sequence, b: Sequence) -> list[Match]:
    return match_b(range(len(a)), a, b)


def my_match_parallel(a: Sequence, b: Sequence) -> list[Match]:
    processes = 11

    matches = []

    with ProcessPoolExecutor(max_workers=processes) as executor:
        for matches_b in executor.map(
            match_b,
            (range(i, len(a), processes) for i in range(processes)),
            repeat(a),
            repeat(b),
        ):
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

    matches = my_match_parallel(token_lyrics, token_dialogue)
    log.info(f"matched {len(matches)}")
    matches.sort(key=lambda m: (m.size, m.a, m.b), reverse=True)
    log.info("sorted")

    for matches_batches in batched(matches, n=1000):
        print(
            "\n".join(
                tokenise.detokenise(token_lyrics[m.a : m.a + m.size]) for m in matches_batches
            ) 
        )
    log.info("done")


if __name__ == "__main__":
    main()
