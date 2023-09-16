import requests
from bs4 import BeautifulSoup


class ProxyScrape:

    def proxyscrapecom(self, type):
        url = "https://proxyscrape.com/free-proxy-list"

        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            table = soup.find('table', class_="table table-striped")
            tHeaders = []
            for header in table.find_all('th'):
                tHeaders.append(header.get_text())

            requestProxies = self.getReq()

            if(type == 'http'):
                proxies = self.getProxies(requestProxies, requestProxies[type], type)
            elif(type == 'socks4'):
                proxies = self.getProxies(requestProxies, requestProxies[type], type)
            elif(type == 'socks5'):
                proxies = self.getProxies(requestProxies, requestProxies[type], type)

            return proxies

        except Exception as e:
            print(f"An error occurred: {e}")

    def getReq(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/116.0.0.0 Safari/537.36',
            'Accept': 'application/json, text/javascript, */*; q=0.01'
        }
        r = requests.get('https://api.proxyscrape.com/proxytable.php?nf=true&country=all', headers=headers)
        return r.json()

    def getProxies(self, requestProxies, req, kind):
        proxies = []
        if kind == 'http':
            for proxy in req:
                if requestProxies[kind][proxy]['uptime'] >= 80 and requestProxies[kind][proxy]['timeout'] <= 500:
                    proxies.append(proxy)
        elif kind == 'socks4' or kind == 'socks5':
            for proxy in req:
                if requestProxies[kind][proxy]['uptime'] >= 80 and requestProxies[kind][proxy]['timeout'] <= 2000:
                    proxies.append(proxy)

        return proxies

    def proxylistcom(self, type):
        url = "https://proxyscrape.com/free-proxy-list"

        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

        except Exception as e:
            print(f"An error occurred: {e}")