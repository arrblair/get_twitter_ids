import re
import requests
from sys import argv

# pass in the url that you need to get the twitter ids from the command line
r = requests.get(argv[1])

ids = re.findall(r'data-item-id="\d*', r.text)

id_numbers = []

for id in ids:
    splitter = id.split('"')
    number = splitter[1]
    id_numbers.append(number)

for number in id_numbers:
    print number
#save for later
