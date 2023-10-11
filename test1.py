#!/usr/bin/python
# All test code

import requests
import subprocess


URL = "https://bbc.co.uk"

r = requests.get(URL)

if r.status_code == 200:
    print(r.text)
else:
    print(f"Error status code {r.status_code}")

command = input("Give a command")

#subprocess.run(command, shell=True)

bad = input("Which dir to list?")

#subprocess.run(bad, shell=True)

