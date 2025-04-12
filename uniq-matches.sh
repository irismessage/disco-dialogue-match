#!/usr/bin/env bash
set -eux

file='textmatchesalluniq.txt'
rm "${file}"
uniq 'textmatches.txt' >> "${file}"
uniq 'textmatchesextra.txt' >> "${file}"
