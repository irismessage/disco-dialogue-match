#!/usr/bin/env python

from bs4 import BeautifulSoup


def get_lyrics(soup: BeautifulSoup) -> str:
    lyrics_block = soup.find(attrs={"data-lyrics-container": "true"})
    paragraphs = lyrics_block.find_all("p")
    return "\n".join("\n".join(p.stripped_strings for p in paragraphs))


def main():
    with open("html/Sea-power-a-light-above-descending-lyrics") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
    print(get_lyrics(soup))


if __name__ == "__main__":
    main()
