#!/usr/bin/env python

from sys import argv

from bs4 import BeautifulSoup


def get_lyrics(soup: BeautifulSoup) -> str:
    lyrics_block = soup.find(attrs={"data-lyrics-container": "true"})
    header = lyrics_block.find("div", attrs={"data-exclude-from-selection": "true"})
    header.clear()
    return "\n".join(lyrics_block.stripped_strings)


def main():
    with open(argv[1]) as f:
        soup = BeautifulSoup(f.read(), "html.parser")
    print(get_lyrics(soup))


if __name__ == "__main__":
    main()
