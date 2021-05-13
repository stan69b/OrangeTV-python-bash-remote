#!/usr/bin/python3

import sys
import requests

USAGE = """Usage: {} <ip> <key>
       ip is available through your livebox's connected devices
       key is the key on the remote that you wish to send (see list of keys)
""".format(sys.argv[0])

if len(sys.argv) < 2:
    print(USAGE)
    sys.exit(1)

ip = sys.argv[1]
key = sys.argv[2]
port = "8080"
timeout = "1000"
url = "http://{}:{}/remoteControl/cmd?operation=01&key={}&mode=0".format(ip, port, key)

# sending get request and saving the response as response object
req = requests.get(url = url)

# extracting data in json format
data = req.json()

# printing the output
print("red : %s" % data)
