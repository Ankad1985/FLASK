import argparse
import asyncio
import aiohttp
import time
import os

img_urls = [
    'https://img.freepik.com/free-photo/a-painting-of-a-mountain-lake-with-a-mountain-in-the-background_188544-9126.jpg',
    'https://w.forfun.com/fetch/21/215e3ddf9d2d722a16e435992d354932.jpeg',
    'https://kartinki.pics/uploads/posts/2023-02/1675745758_kartinkin-net-p-khaski-mototsikl-pinterest-1.jpg',
    'https://images.wallpaperscraft.ru/image/single/doroga_ravnina_gory_1157718_1280x720.jpg'
]

IMG_DIR = 'images'


async def download_image(url, target_dir: str):
    start_process_time = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.read()
            filename = url.split('/')[-1]
            with open(os.path.join(target_dir, filename), 'wb') as img:
                img.write(data)
            print(f"Downloaded {url} in {time.time() - start_process_time:.2f} seconds")


async def main():
    tasks = []
    for img_url in urls:
        tasks.append(asyncio.create_task(download_image(img_url, IMG_DIR)))
    await asyncio.gather(*tasks)


def parse():
    parser = argparse.ArgumentParser(
        description='Downloads images from given url list')
    parser.add_argument('-u', '--urls', nargs='+', type=str,
                        help='Image URLs separated by space')
    return parser.parse_args()


if __name__ == '__main__':
    urls = parse().urls or img_urls

    if not os.path.exists(IMG_DIR):
        os.mkdir(IMG_DIR)

    start_time = time.time()
    asyncio.run(main())

    print(f'Total download time (async): {time.time() - start_time:.2f} sec')
