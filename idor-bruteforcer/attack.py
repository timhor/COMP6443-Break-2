# fill in the relevant fields for the cookies dict before running

import requests
import sys

cookies={'zid': '', 'token': ''}

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()
    for line in lines:
        number = line.strip()
        r = requests.post('http://pastebing.ns.agency/raw/2uL' + line, cookies=cookies)
        if r.status_code != 404:
            print(r.text)
