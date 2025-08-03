#!/usr/bin/env python3

import sys
import re
import subprocess

prefix = sys.argv[1]
cmd = f'''
curl --location --silent http://www.timetable.unsw.edu.au/2024/{prefix}KENS.html |
grep -E "href=\\"{prefix}[0-9]{{4}}\\.html\\"" |
sed -E 's/ +<//' |
sed -E 's/td class=\\"data\\"><a href=\\"//' |
sed -E 's/\\">/ /' |
sed -E 's/\\.html//' |
sed -E 's#</a></td>##' |
sed -E "s/{prefix}[0-9]{{4}} {prefix}[0-9]{{4}}//g" |
sed -E '/^$/d' |
sort -k1 |
uniq
'''

result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
print(result.stdout, end="")
