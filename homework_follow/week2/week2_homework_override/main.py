from channel_extract import channels
from page_parsing import get_item_url, item_info
from multiprocessing import Pool


def get_item_urls(channels):
    for i in range(1, 5):
        get_item_url(channels, i)

if __name__ == '__main__':

    p = Pool()
    p.map(get_item_urls, channels)
    p.close()
    p.join()
