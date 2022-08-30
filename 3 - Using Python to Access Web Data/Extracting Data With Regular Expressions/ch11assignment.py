#Code for practice data
import re

doc = open('regex_sum_42.txt')

sum1 = 0

for line in doc:
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        sum = sum1 + int(number)

print(sum)

#Code for assignment data
doc2 = open('regex_sum_1419494.txt')

sum2 = 0

for line in doc2:
    numbers2 = re.findall('[0-9]+', line)
    for number2 in numbers2:
        sum3 = sum2 + int(number2)

print(sum3)
