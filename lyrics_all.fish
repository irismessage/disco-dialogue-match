#!/usr/bin/env fish
for f in html/*; ./lyrics_from_html.py "$f" >> all-lyrics.txt; end
