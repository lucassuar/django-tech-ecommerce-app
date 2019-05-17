from django.test import TestCase
from .models import Order

# Create your tests here.
class OrderTests(TestCase):
  
    def date_str_test(self):
        test_order = Order(full_name= "test", 
                    phone_number= "test", 
                    country="test",
                    postcode= "test",
                    town_or_city= "test",
                    street_address1= "test",
                    street_address2="test",
                    date="2020-10-10")
                    
        self.assertEqual(str(test_order.date), "2020-10-10")