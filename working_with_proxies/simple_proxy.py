import requests

# google might block the free proxy
proxy = '208.82.61.12:3128'

print("Using proxy for httpbin")
r = requests.get("https://httpbin.org/ip",
                 proxies={
                     "http": proxy,
                     "https": proxy
                 },
                 timeout=3
                 )
print(r.status_code)
print(r.json())

# free proxy
# https://free-proxy-list.net/
print()
print("Trying on google")
try:
    r = requests.get("https://google.co.uk",
                 proxies={
                     "http": proxy,
                     "https": proxy
                 },
                 timeout=3
                 )
    print(r.status_code)
    print(r.content)
    # print(r.content)
except:
    print("The google one failed")
    