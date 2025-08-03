#!/usr/bin/env python3

import sys
import re

pattern = sys.argv[1]
filename = sys.argv[2]

with open(filename, "r") as f:
    for line in f:
        if re.search(pattern, line):
            print(line, end="")
