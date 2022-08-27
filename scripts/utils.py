import fcntl
import json
import os
import pathlib
from bs4 import BeautifulSoup
import requests

def get_json(url):
    content = requests.get(url).content
    return json.loads(content)

def get_html(url) -> BeautifulSoup:
    content = requests.get(url).content
    return BeautifulSoup(content, 'html.parser', from_encoding='utf-8')

def tag2path(tag):
    download_dir = f'/home/yibo/CRYPTOREX/CRYPTOREX_criticism/download/{tag}'
    pathlib.Path(download_dir).mkdir(parents=True, exist_ok=True)
    return download_dir

def count_downloaded(tag):
    download_dir = tag2path(tag)
    return len(os.listdir(download_dir))

def download_firmware(url, tag):
    download_dir = tag2path(tag)
    os.chdir(download_dir)
    print(f'[-] Downloading: {url}')
    os.system(f'wget -q -nc --no-check-certificate "{url}"')
    
def download_all(urls, tag):
    for i, url in enumerate(urls):
        print(f'[*] Downloading... ({i + 1}/{len(urls)})')
        download_firmware(url, tag)
        
def cache_url(url, tag):
    with open(f'cache/{tag}.txt', 'a') as fd:
        fcntl.flock(fd, fcntl.LOCK_EX)
        fd.write(url + '\n')
        fd.flush()
        fcntl.flock(fd, fcntl.LOCK_UN)