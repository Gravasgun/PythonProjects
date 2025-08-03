#!/usr/bin/env python3

import requests
import sys
from bs4 import BeautifulSoup
import re

course_dict = dict()
prefix = sys.argv[1]
url = f"http://www.timetable.unsw.edu.au/2024/{prefix}KENS.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html5lib")

a_lists = soup.find_all("a")

for tag in a_lists:
    href = tag.get("href")
    course_name = tag.text.strip()
    if href != None and re.match(rf"{prefix}[0-9]{{4}}\.html", href):
        course_code = href.replace(".html", "")
        course_dict[course_code] = course_name

for code in sorted(course_dict.keys()):
    print(f"{code} {course_dict[code]}")
