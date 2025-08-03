#!/bin/dash

prefix="$1"

curl --location --silent http://www.timetable.unsw.edu.au/2024/${prefix}KENS.html |
grep -E "href=\"${prefix}[0-9]{4}\.html\"" |
sed -E 's/ +<//' |
sed -E 's/td class=\"data\"><a href=\"//'|
sed -E 's/\">/ /' |
sed -E 's/\.html//' |
sed -E 's/<\/a><\/td>//' |
sed -E "s/${prefix}[0-9]{4} ${prefix}[0-9]{4}//g" |
sed -E '/^$/d' |
sort -k1 |
uniq

# 容易出错的点：
# 1.想在正则表达式中匹配 " 号，需要写 \"（是为了让 shell 正确传递引号）
# 2.想匹配 . 字符（而不是任意字符），正则中要写 \.
# 3.正则表达式中引用变量要用 ${变量}，以明确变量边界，避免出错
# 4.单引号内的内容不会展开变量；需要引用变量时必须使用双引号