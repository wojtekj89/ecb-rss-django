from django.test import TestCase
from .services import ECBScraper

class ScraperTest(TestCase):
    def setUp(self):
        self.s = ECBScraper()
    
    def test_reading_data(self):
        data = self.s.read_data('usd')
        print(data)
        self.assertTrue('USD' in str(data))
