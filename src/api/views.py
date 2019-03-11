from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND

from .models import ExchangeRate

from .serializers import ExchangeRateSerializer

import datetime

class AllRates(ListAPIView):
    serializer_class = ExchangeRateSerializer

    def get_queryset(self):
        currency = self.request.query_params.get('currency')

        if not currency:
            return ExchangeRate.objects.all()

        qs = ExchangeRate.objects.filter(currency=str(currency).upper())
        # TODO: handle when filtering with wrong currency

        return qs

class TodayRates(ListAPIView):
    serializer_class = ExchangeRateSerializer

    def get_queryset(self):
        today = datetime.datetime.now()
        qs = ExchangeRate.objects.filter(date=today.date())

        if not qs:
            yesterday = today - datetime.timedelta(days = 1)
            qs = ExchangeRate.objects.filter(date=yesterday.date())

        return qs
