import json
from urllib.request import urlopen

address = input('Enter an address - ')
if address == '':
    quit()
data = urlopen(address).read()

data = json.loads(data)

total = 0
for user in data['comments']:
    total = total + user['count']

print('Total comments:', total)
