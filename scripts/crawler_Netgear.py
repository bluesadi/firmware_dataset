from utils import cache_url, get_html, get_json
import multiprocessing as mp

def retrieve_one(url):
    download_page = get_html(url)
    for div_label in download_page.find_all('div', class_='accordion-item'):
        for title_label in div_label.find_all('a', class_='accordion-title'):
            if 'Firmware' in title_label.text:
                for download_label in div_label.find_all('a', href=lambda href : href is not None and href.endswith('.zip')):
                    download_url = download_label['href']
                    cache_url(download_url, 'Netgear')
                    print(download_url)
                    return

if __name__ == '__main__':
    pool = mp.Pool(processes=mp.cpu_count())
    tasks = list()
    models = get_json('https://www.netgear.com/system/supportModels.json')
    for model in models:
        url = model['url']
        if url.startswith('/support/product'):
            url = f'https://www.netgear.com{url}'
            task = pool.apply_async(func=retrieve_one, args=(url,))
            tasks.append(task)
    pool.close()
    pool.join()
    for task in tasks:
        task.wait()
    print('Done!')