import pprint
import requests
from bs4 import BeautifulSoup
import sys
import csv

class ProxyScrape:

    def proxy_scrape_com(self, type):
        url = "https://proxyscrape.com/free-proxy-list"

        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            table = soup.find('table', class_="table table-striped")

            request_proxies = self.get_req()

            proxies = self.get_proxies(request_proxies, request_proxies[type], type)

            return proxies

        except Exception as e:
            print(f"An error occurred: {e}")

    def get_req(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/116.0.0.0 Safari/537.36',
            'Accept': 'application/json, text/javascript, */*; q=0.01'
        }
        r = requests.get('https://api.proxyscrape.com/proxytable.php?nf=true&country=all', headers=headers)
        return r.json()

    def get_proxies(self, request_proxies, req, kind):
        proxies = []
        if kind == 'http':
            for proxy in req:
                if request_proxies[kind][proxy]['uptime'] >= 80 and request_proxies[kind][proxy]['timeout'] <= 500:
                    proxies.append(proxy)
        elif kind == 'socks4' or kind == 'socks5':
            for proxy in req:
                if request_proxies[kind][proxy]['uptime'] >= 80 and request_proxies[kind][proxy]['timeout'] <= 2000:
                    proxies.append(proxy)

        return proxies

    def proxy_list_com(self):
        url = "https://free-proxy-list.net/"

        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            table = soup.find('table', class_="table table-striped table-bordered")
            table_body = soup.find('tbody')

            headers = self.process_header(table)
            to_export = self.process_body(table_body, headers)

            self.export_to_csv(to_export)

        except Exception as e:
            print(f"An error occurred: {e}")

    def process_header(self, table):
        t_headers = []
        for header in table.find_all('th'):
            t_headers.append(header.get_text())

        return t_headers

    def process_body(self, table_body, headers):
        to_return = []
        for row in table_body.find_all('tr'):
            rows = []
            for cell in row.find_all('td'):
                rows.append(cell.text.strip())
            to_return.append(rows)

        to_return.insert(0, headers)

        return to_return

    def export_to_csv(self, to_export):
        try:
            pprint.pprint(to_export)
            csv_file_path = 'proxies.csv'

            with open(csv_file_path, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                for row in to_export:
                    csv_writer.writerow(row)

        except Exception as e:
            print(f"An error occurred: {e}")
