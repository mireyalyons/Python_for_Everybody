#Chapter 11 - Regular Expressions Assignment

import re

doc = open('regex_sum_1419494.txt')

sum = 0

for line in doc:
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        sum = sum + int(number)

print(sum)
