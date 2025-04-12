#!/usr/bin/env bash
set -eux

dir='dialogue-process'
mkdir -p "${dir}"

tr '[:upper:]' '[:lower:]' < 'dialoguetext.txt' > "${dir}/1-lower.txt"
tr  --delete '[:punct:]' < "${dir}/1-lower.txt" > "${dir}/2-no-punctuation.txt"
tr --squeeze-repeats '[:space:]' < "${dir}/2-no-punctuation.txt" > "${dir}/3-squeeze-space.txt"
tr '[:space:]' ' ' < "${dir}/3-squeeze-space.txt" > "${dir}/4-regular-space.txt"

cp "${dir}/4-regular-space.txt" "${dir}/done.txt"
