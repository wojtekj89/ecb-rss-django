from core import settings
import requests
from decimal import Decimal
from dateutil.parser import parse
from bs4 import BeautifulSoup

class ECBScraper:

    def __init__(self):
        self.url = settings.ECB_URL

    def read_data(self, currency):
        r = requests.get(self.url.format(currency))

        if not r.status_code == 200:
            return
            # TODO: handle scraper error

        parser = BeautifulSoup(response, 'lxml')
        item = parser.find('item')

        return self.parse_response(item)

    def parse_response(self, item):
        stats = item.find('cb:statistics')
        currency = stats.find('cb:targetcurrency').text
        rate = stats.find('cb:value').text
        date = parse(item.find('dc:date').text)

        return {
            'currency': currency,
            'rate': float(rate),
            'date': date
        }
    
    def read_archive_data(self, currency):
        r = requests.get(self.url.format(currency))

        if not r.status_code == 200:
            return
            # TODO: handle scraper error
        
        parser = BeautifulSoup(r.content, 'lxml')
        items = parser.find_all('item')
        rates = list()
        for item in items:
            rates.append(self.parse_response(item))
        
        return rates