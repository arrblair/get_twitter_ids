import re
import requests
from sys import argv


r = requests.get(argv[1])
text = r.text

ids = re.findall(r'data-item-id="\d*', r.text)
for id in ids:
    splitter = id.split('"')
    number = splitter[1]
    print number
