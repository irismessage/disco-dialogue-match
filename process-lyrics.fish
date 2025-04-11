#!/usr/bin/env fish
tr '[:upper:]' '[:lower:]' < all-lyrics.txt > lyrics-process/lower.txt
sed 's/[^a-z ]//g' lyrics-process/lower.txt > lyrics-process/alpha-only.txt
tr '\n' ' ' < lyrics-process/alpha-only.txt > lyrics-process/no-newlines.txt
cp lyrics-process/no-newlines.txt lyrics-process/done.txt
