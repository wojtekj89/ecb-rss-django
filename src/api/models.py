from django.db.models import Model, CharField, FloatField, DateField

class ExchangeRate(Model):
    currency = CharField(max_length=10)
    rate = FloatField()
    date = DateField()
    