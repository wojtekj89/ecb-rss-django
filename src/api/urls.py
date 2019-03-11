from django.conf.urls import url

from .views import AllRates, TodayRates

urlpatterns = [
    url(r'all', AllRates.as_view(), name='all_rates_list'),
    url(r'today', TodayRates.as_view(), name='today_rates_list')
]