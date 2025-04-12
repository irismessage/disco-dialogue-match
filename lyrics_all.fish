#!/usr/bin/env fish

rm all-lyrics.txt
for f in html/*; ./lyrics_from_html.py "$f" >> all-lyrics.txt; end
