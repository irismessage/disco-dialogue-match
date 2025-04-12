#!/usr/bin/env bash
dir='dialogue-process'
tr '[:upper:]' '[:lower:]' < 'dialoguetext.txt' > "${dir}/lower.txt"
tr  --delete '[:punct:]' < "${dir}/lower.txt" > "${dir}/no-punctuation.txt"
tr --squeeze-repeats '[:space:]' < "${dir}/no-punctuation.txt" > "${dir}/squeeze-space.txt"
tr '[:space:]' ' ' < "${dir}/squeeze-space.txt" > "${dir}/regular-space.txt"
cp "${dir}/regular-space.txt" "${dir}/done.txt"
