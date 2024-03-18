import requests
from multiprocessing import Process, Pool
import time
import argparse

parser = argparse.ArgumentParser(description='Download images')
parser.add_argument('urls', nargs='+')
args = parser.parse_args()
urls = args.urls

start_time = time.time()

def download(url):
    response = requests.get(url)
    with open(f'hw04/images/{url.split("/")[-1]}', 'wb') as file:
        file.write(response.content)
    print(f'Downloaded {url.split("/")[-1]} in {time.time()-start_time:.2f}seconds')


processes = []

if __name__ == '__main__':
    for url in urls:
        process = Process(target=download, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f"Images were downloaded in {time.time()-start_time:.2f}seconds")