from requests import ReadTimeout, ConnectTimeout
from requests.exceptions import ProxyError

import requests
import csv

URL = "https://httpbin.org/ip"
TIMEOUT_IN_SECONDS = 10
CSV_FILENAME = "more_rotating_proxy_use_case/proxies.csv"

with open(CSV_FILENAME) as f:
    reader = csv.reader(f)
    for csv_row in reader:
        scheme_proxy_map = {
            "https": csv_row[0]
        }


# scheme_proxy_map = {
#     "http": PROXY1,
#     "https": PROXY2,
#     "https://example.org": PROXY3,
# }

try:
    response = requests.get(URL, proxies=scheme_proxy_map,
                            timeout=TIMEOUT_IN_SECONDS)
except (ProxyError, ReadTimeout, ConnectTimeout) as err:
    print("Unable to connect to the proxy: ", err)
else:
    print(response.text)