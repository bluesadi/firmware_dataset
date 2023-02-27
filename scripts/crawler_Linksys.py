from utils import cache_url, get_html
import multiprocessing as mp

def retrieve_one(url):
    product_page = get_html(url)
    for product_label in product_page.find_all('a', title='DOWNLOADS / FIRMWARE'):
        download_page = get_html(product_label['href'])
        for download_label in download_page.find_all('a', href=lambda href: href is not None and href.startswith('https://downloads.linksys.com/downloads/firmware/')):
            download_url = download_label['href']
            cache_url(download_url, 'Linksys')
            print(download_url)
            return

if __name__ == '__main__':
    pool = mp.Pool(processes=mp.cpu_count())
    tasks = list()
    html = get_html('https://www.linksys.com/sitemap')
    for label in html.find_all('a', attrs={'class': 'sitemap-list__link'}):
        task = pool.apply_async(func=retrieve_one, args=(label['href'],))
    pool.close()
    pool.join()
    for task in tasks:
        task.wait()
    print('Done!')