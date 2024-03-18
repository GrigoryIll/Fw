import asyncio
import aiohttp
import time
import argparse


async def download(url):
    async with aiohttp.ClientSession() as session:  
        async with session.get(url) as response:
            pic = await response.read()
            with open(f'hw04/images/{url.split("/")[-1]}', 'wb') as file:
                file.write(pic)
            print(f'Downloaded {url.split("/")[-1]} in {time.time()-start_time:.2f}seconds')


async def main(urls):
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)

start_time = time.time()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download images')
    parser.add_argument('urls', nargs='+')
    args = parser.parse_args()
    asyncio.run(main(args.urls))
    print(f"Images were downloaded in {time.time()-start_time:.2f}seconds")