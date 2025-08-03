#!/usr/bin/env python3
import statistics
import sys

str_number = sys.argv[1:]
numbers = list(map(int, str_number))
number_set = set()
count = len(numbers)
product = 1
for number in numbers:
    number_set.add(number)
    product *= number
unique = len(number_set)
minimum = min(numbers)
maximum = max(numbers)
mean = statistics.mean(numbers)
median = statistics.median(numbers)
mode = statistics.mode(numbers)
sum = sum(numbers)
print(f"count={count}")
print(f"unique={unique}")
print(f"minimum={minimum}")
print(f"maximum={maximum}")
print(f"mean={mean}")
print(f"median={median}")
print(f"mode={mode}")
print(f"sum={sum}")
print(f"product={product}")
