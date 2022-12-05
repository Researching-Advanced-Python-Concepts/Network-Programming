import requests
import csv
import concurrent.futures

proxy_file_path = "working_with_proxies/proxy.csv"
proxylist = []

with open(proxy_file_path, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        proxylist += row

# print(len(proxylist))
def extract(proxy):
    try:
        print("Using proxy: ", proxy)
        r = requests.get(
            "https://httpbin.org/ip", proxies={"http": proxy, "https": proxy}, timeout=5
        )
        print(r.status_code)
        if r.status_code:
            print()
            print("Data for proxy: ", proxy)
            print(r.json())
    except Exception as err:
        print()
        print(err)
        print(err.__dir__())
    return proxy

# extract(proxylist[0])
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(extract, proxylist)
