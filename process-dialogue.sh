#!/usr/bin/env bash
set -eux

in_file='dialoguetextextra.txt'
dir='dialogue-process'
mkdir -p "${dir}"

tr '[:upper:]' '[:lower:]' < "${in_file}" > "${dir}/1-lower.txt"
tr  --delete '[:punct:]' < "${dir}/1-lower.txt" > "${dir}/2-no-punctuation.txt"
tr '[:space:]' ' ' < "${dir}/2-no-punctuation.txt" > "${dir}/3-regular-space.txt"
tr --squeeze-repeats '[:space:]' < "${dir}/3-regular-space.txt" > "${dir}/4-squeeze-space.txt"

cp "${dir}/4-squeeze-space.txt" "${dir}/done.txt"
