import requests
from bs4 import BeautifulSoup
import sys

def find_paths(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        paths = []
        for link in links:
            href = link.get('href')
            if href:
                if href.startswith('http://') or href.startswith('https://'):
                    paths.append(href)
                else:
                    path = url + href
                    paths.append(path)
        return paths
    else:
        print('Lỗi:', response.status_code)
        return []

url = sys.argv[1]
paths = find_paths(url)
for path in paths:
    print(path)
