# Network Programming

## Rotating Proxies

- By rotating proxy IP addresses, we can enhance our anonymity, imitate the behavior of several organic users, and circumvent most anti-scraping measures.
- [get proxies](https://free-proxy-list.net/)

### Using Proxy

- Basic Format: `SCHEME://USERNAME:PASSWORD@PROXY_IP:PROXY_PORT`
- eg:

  - `http:2.57.214.230:3222`
  - `https:2.57.215.230:8092`
  - `https://user1:pokemon@2.56.215.230:8045`

- we can specify multiple protocols and even define specific domains for which a diff. proxy will be used

- ```py
    scheme_proxy_map = {
        "http": PROXY1,
        "https": PROXY2,
        "https://example.org": PROXY3,
    }
  ```
