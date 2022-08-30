# Run seperately

#Code for Chaper 11 Assignment Data

import re

doc = open('regex_sum_1419494.txt')

sum = 0

for line in doc:
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        sum = sum + int(number)

print(sum)


#Code for Practice Data

import re

doc = open('regex_sum_42.txt')

sum1 = 0

for line in doc:
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        sum = sum1 + int(number)

print(sum)
