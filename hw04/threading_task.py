import threading
import requests
import time
import argparse


parser = argparse.ArgumentParser(description='Download images')
parser.add_argument('urls', nargs='+')
args = parser.parse_args()
urls = args.urls

threads = []
start_time = time.time()

def download(url):
    response = requests.get(url)
    with open(f'hw04/images/{url.split("/")[-1]}', 'wb') as file:
        file.write(response.content)
    print(f'Downloaded {url.split("/")[-1]} in {time.time()-start_time:.2f}seconds')

for url in urls:
    thread = threading.Thread(target=download, args=[url])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Images were downloaded in {time.time()-start_time:.2f}seconds")