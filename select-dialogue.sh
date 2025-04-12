#!/usr/bin/env bash
set -eux

sqlite3 'discobase12-17-2021-4-18-51-PM.db' 'SELECT dialoguetext FROM dentries;' > dialoguetext.txt
