#!/usr/bin/env fish
tr '[:upper:]' '[:lower:]' < dialoguetext.txt > dialogue-process/lower.txt
sed 's/[^a-z ]//g' dialogue-process/lower.txt > dialogue-process/alpha-only.txt
tr '\n' ' ' < dialogue-process/alpha-only.txt > dialogue-process/no-newlines.txt
cp dialogue-process/no-newlines.txt dialogue-process/done.txt
