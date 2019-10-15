from bs4 import BeautifulSoup

import requests
import os


urls = []
path = os.path.expanduser('output-files/')

if os.path.isdir(path):
    pass
else:
    os.mkdir(path)

with open('urls.txt') as f:
    for line in f:
        urls.append(line.rstrip('\n'))

for url in urls:
    print(url)
    page = requests.get(url)

    # Create BeautifulSoup object
    soup = BeautifulSoup(page.text, 'html.parser')
    result = soup.find("div", {"id": "output"})
    # print(result)

    outfile = url.split('/reference/')[1].replace('/', '-')
    file_path = os.path.join(path, outfile)
    print('File Created: ', outfile)
    with open(file_path, 'w') as out_file:
        for line in str(result):
            out_file.write(line)
