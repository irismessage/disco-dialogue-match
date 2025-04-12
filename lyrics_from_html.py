#!/usr/bin/env python

from sys import argv

from bs4 import BeautifulSoup


def get_lyrics(soup: BeautifulSoup) -> str:
    lyrics_block = soup.find(attrs={"data-lyrics-container": "true"})
    header = lyrics_block.find("div", attrs={"data-exclude-from-selection": "true"})
    header.clear()

    lyrics_lines = list(lyrics_block.stripped_strings)

    title = (
        soup.find("title")
        .string.removeprefix("Sea Power – ")
        .removesuffix(" Lyrics | Genius Lyrics")
    )
    lyrics_lines.insert(0, title)

    return "\n".join(lyrics_lines)


def main():
    with open(argv[1]) as f:
        soup = BeautifulSoup(f.read(), "html.parser")
    print(get_lyrics(soup))


if __name__ == "__main__":
    main()
