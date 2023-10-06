#!/usr/bin/python
# All test code

import requests


URL = "https://bbc.co.uk"

r = requests.get(URL)

if r.status_code == 200:
    print(r.text)
else:
    print(f"Error status code {r.status_code}")

