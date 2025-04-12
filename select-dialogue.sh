#!/usr/bin/env bash
set -eux

file='discobase12-17-2021-4-18-51-PM.db'

sqlite3 \
    "${file}" \
    "SELECT dialoguetext FROM dentries WHERE dialoguetext <> '0';"
