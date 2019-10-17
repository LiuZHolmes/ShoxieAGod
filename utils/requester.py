import urllib3


def send_request(method, url):
    http = urllib3.PoolManager()
    return http.request(method, url)
