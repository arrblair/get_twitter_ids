import requests
from sys import argv


r = requests.get(argv[1])
text = r.text
parse_me = text.split('</')

for element in parse_me:
    if 'data-item-id' in element:
        splitter = element.split('=')
        number = splitter[1]
        split_whole_id = whole_id.split('')
        print number
