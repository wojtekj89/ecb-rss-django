from __future__ import absolute_import, unicode_literals

from celery import shared_task
from celery.signals import celeryd_init

from core import settings
from api.models import ExchangeRate
from api.services import ECBScraper


@celeryd_init.connect
def at_start(sender, **k):
    """ Getting archive data on start of the app """
    get_history_exchange_rates.delay()

@shared_task
def get_exchange_rates():
    currencies = settings.CURRENCIES
    scraper = ECBScraper()

    for currency in currencies:
        data = scraper.read_data(currency)
        rate = ExchangeRate(currency=data.get('currency'), rate=float(data.get('rate')), date=data.get('date'))

        try:
            rate.save()
        except Exception as e:
            # TODO: handle error in saving
            print('saving error ', str(e))
            pass
    
    return

@shared_task
def get_history_exchange_rates():
    currencies = settings.CURRENCIES
    scraper = ECBScraper()

    for currency in currencies:
        data = scraper.read_archive_data(currency)

        for item in data:
            rate = ExchangeRate(currency=item.get('currency'), rate=float(item.get('rate')), date=item.get('date'))

            try:
                rate.save()
            except Exception as e:
                # TODO: handle error in saving
                print('saving error ', str(e))
                pass
    
    return