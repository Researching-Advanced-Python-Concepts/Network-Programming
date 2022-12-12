# for speed
import aiohttp
import asyncio
import csv

URL = "https://httpbin.org/ip"
TIMEOUT_IN_SECONDS = 10
CSV_FILENAME = "more_rotating_proxy_use_case/proxies.csv"

with open(CSV_FILENAME) as f:
    reader = csv.reader(f)
    for csv_row in reader:
        scheme_proxy_map = {
            "https": csv_row[0],
            "http": csv_row[0]
        }


async def check_proxy(url, proxy):
    # try:
        session_timeout = aiohttp.ClientTimeout(total=None,
                                                sock_connect=TIMEOUT_IN_SECONDS,
                                                sock_read=TIMEOUT_IN_SECONDS)
        async with aiohttp.ClientSession(timeout=session_timeout, trust_env=True) as session:
            async with session.get(url, proxy=proxy, timeout=TIMEOUT_IN_SECONDS) as resp:
                    print(await resp.text())
    # except Exception as error:
    #     # comment this out to only see valid proxies printed out in
    #     # the command line
    #     print()
    #     print(proxy)
    #     print("Proxy responded with an error: ", error)
        return


async def main():
    tasks = []
    with open(CSV_FILENAME) as f:
        reader = csv.reader(f)
        for csv_row in reader:
            task = asyncio.create_task(
                check_proxy(URL, csv_row[0])
            )
            tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())