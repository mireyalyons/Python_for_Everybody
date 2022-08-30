#Code for practice data
import re

doc = open('py4ech11sampledata.txt')

sum = 0

for line in doc:
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        sum = sum + int(number)

print(sum)



#Code for assignment data
import re

doc2 = open('ch11actualdata.txt')

sum2 = 0

for line in doc2:
    numbers2 = re.findall('[0-9]+', line)
    for number2 in numbers2:
        sum3 = sum2 + int(number2)

print(sum3)
