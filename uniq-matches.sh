#!/usr/bin/env bash
set -eux

uniq 'textmatches.txt' > 'textmatches-uniq.txt'
uniq 'textmatchesextra.txt' > 'textmatchesextra-uniq.txt'
