from django.test import TestCase
from .forms import MakePaymentForm, OrderForm


class TestOrderForm(TestCase):
    
    def test_can_make_a_payment_with_required_values(self):
        form = OrderForm({
                    'full_name': "test", 
                    'phone_number': "test", 
                    'country': "test",
                    'postcode': "test",
                    'town_or_city': "test",
                    'street_address1': "test",
                    'street_address2': "test",
                    'county': 'test'
                    
        })
        self.assertTrue(form.is_valid())


class TestMakePaymentForm(TestCase):
    
    def test_can_make_a_payment_with_required_values(self):
        form = MakePaymentForm({
                    'credit_card_number': '4242424242424242', 
                    'cvv': "111",
                    'expiry_month': 1,
                    'expiry_year': 2020,
                    'stripe_id': 'l' #This id is a test value but is used correctly on the actual page
        })
        self.assertTrue(form.is_valid())
        
    def test_cannot_make_a_payment_with_required_values(self):
        form = MakePaymentForm({
                    'credit_card_number': '4242424242424242', 
                    'cvv': "111", 
                    'expiry_month': 1,
                    'expiry_year': 2020,
        })
        self.assertFalse(form.is_valid())
    