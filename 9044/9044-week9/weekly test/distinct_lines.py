#!/usr/bin/env python3

import sys
import re

line_number = int(sys.argv[1])
line_dict = dict()
count = 0

for line in sys.stdin:
    new_line = re.sub(r"\s*", "", line.lower().strip())
    if new_line not in line_dict:
        line_dict[new_line] = 1
    else:
        line_dict[new_line] += 1
    count += 1
    if len(line_dict) >= line_number:
        print(f"{line_number} distinct lines seen after {count} lines read.")
        break
else:
    # 输入结束了，没达到目标数量
    print(f"End of input reached after {count} lines read - {line_number} different lines not seen.")
