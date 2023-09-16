from __future__ import print_function, unicode_literals
from proxyScrape import ProxyScrape
from pyscreen import PyScreen
import pprint


def main():
    py_screen = PyScreen()
    # unlock = py_screen.unlock()

    chosen_platform = py_screen.input_platforms()
    chosen_type = py_screen.input_type()

    scraper = ProxyScrape()
    if chosen_platform == 'ProxyBay':
        proxies = scraper.proxyscrapecom(chosen_type)

    elif platform == 'Markless':
        proxies = scraper.proxylistcom(chosen_type)

    # pprint.pprint(proxies)

if __name__ == "__main__":
    main()
