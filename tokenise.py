#!/usr/bin/env python

import json
from pathlib import Path
from sys import argv
from typing import Self, Union

PathLike = Union[str, Path]

TABLE_FILE = "token_mapping.json"


class TokenTable:
    def __init__(self):
        self.word_to_token: dict[str, int] = {}
        self.token_to_word: dict[int, str] = {}
        self.tokenised_words: set[str] = set()
        self.next_token = 1

    @classmethod
    def load(cls, fp: PathLike) -> Self:
        table = cls()
        with open(fp) as f:
            table.word_to_token = json.load(f)
        table.token_to_word = {v: k for k, v in table.word_to_token.items()}
        table.tokenised_words = set(table.word_to_token.keys())
        table.next_token = len(table.tokenised_words)

        return table

    def save(self, fp: PathLike):
        with open(fp, "w") as f:
            json.dump(self.word_to_token, f)

    def tokenise_text(self, text: str) -> list[int]:
        words = text.split()
        tokens = []
        for w in words:
            if w not in self.tokenised_words:
                self.word_to_token[w] = self.next_token
                self.token_to_word[self.next_token] = w
                self.next_token += 1
                self.tokenised_words.add(w)
            tokens.append(self.word_to_token[w])

        return tokens

    def detokenise_text(self, tokens: list[int]) -> str:
        return " ".join(self.token_to_word[t] for t in tokens)


def get_table() -> TokenTable:
    try:
        table = TokenTable.load(TABLE_FILE)
    except FileNotFoundError:
        table = TokenTable()
    return table


def tokenise(text: str) -> list[int]:
    table = get_table()

    tokens = table.tokenise_text(text)
    table.save(TABLE_FILE)

    return tokens


def detokenise(tokens: list[int]) -> str:
    table = get_table()
    return table.detokenise_text(tokens)


def main():
    with open(argv[1]) as f:
        text = f.read()
    tokens = tokenise(text)
    print(tokens)
    retext = detokenise(tokens)
    print(retext)
    assert text == retext



if __name__ == "__main__":
    main()
