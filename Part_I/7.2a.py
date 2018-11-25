#!/usr/bin/env python3

from sys import argv

FILEARG = argv[-1]
CONFIG_TXT = open(FILEARG, 'r')
ignore = ['duplex', 'alias', 'Current configuration']
for LINES in CONFIG_TXT:
    if not LINES.startswith('!') and not ignore[0] in LINES and not ignore[1] in LINES and not ignore[2] in LINES:
      print(LINES.strip())
CONFIG_TXT.close()
