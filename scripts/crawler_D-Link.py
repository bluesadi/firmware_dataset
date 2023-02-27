from webbrowser import get
from utils import *
import multiprocessing as mp

def retrieve_one(url):
    dlink_url = 'https://support.dlink.com'
    html = get_html(url)
    for label in html.find_all("a"):
        href = label['href']
        if href is not None and '_FIRMWARE_' in href and (href.endswith('.zip') or href.endswith('.ZIP')):
            download_url = dlink_url + href
            print(download_url)
            cache_url(download_url, "D-Link")
            return

if __name__ == '__main__':
    pool = mp.Pool(processes=mp.cpu_count())
    tasks = list()
    dlink_url = 'https://support.dlink.com'
    html = get_html(f'{dlink_url}/resource/PRODUCTS/')
    for label in html.find_all('a'):
        for sub_dir in ['REVA', 'REVA/FIRMWARE']:
            url = dlink_url + label['href'] + sub_dir
            task = pool.apply_async(func=retrieve_one, args=(url,))
            tasks.append(task)
    pool.close()
    for task in tasks:
        task.wait()
    print('Done!')
            