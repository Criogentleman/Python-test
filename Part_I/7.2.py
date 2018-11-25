#!/usr/bin/env python3

from sys import argv

FILEARG = argv[-1]
CONFIG_TXT = open(FILEARG, 'r')
for LINES in CONFIG_TXT:
    if not LINES.startswith('!'):
        print(LINES.strip())
CONFIG_TXT.close()
