import json
import os

import fcntl
from bs4 import BeautifulSoup
import requests

proxies = {
    "http": os.environ["http_proxy"],
    "https": os.environ["https_proxy"]
}

def get_json(url):
    content = requests.get(url).content
    return json.loads(content)

def get_html(url) -> BeautifulSoup:
    content = requests.get(url, proxies=proxies).content
    return BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
        
def cache_url(url, tag):
    with open(f'cache/{tag}.txt', 'a') as fd:
        fcntl.flock(fd, fcntl.LOCK_EX)
        fd.write(url + '\n')
        fd.flush()
        fcntl.flock(fd, fcntl.LOCK_UN)