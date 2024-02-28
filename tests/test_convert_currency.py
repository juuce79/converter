import unittest
import inspect
from model.converters.convert_currency import CurrencyConverter
from model.converters.custom_error_handling.currency_errors import InvalidCurrencyError


class CurrencyConversionTests(unittest.TestCase):

    def setUp(self):
        self.converter = CurrencyConverter()

    @staticmethod
    def print_output(from_currency, to_currency, value, expected, actual):
        test_method_name = inspect.stack()[1][3]
        print(f"{test_method_name}: {value} {from_currency} = {actual} {to_currency} (Expected: {expected})")

    def test_usd_to_eur(self):
        rate = self.converter.get_exchange_rate('USD', 'EUR')  # Fetch live rate
        result = self.converter.convert_currency('USD', 'EUR', 100)
        expected = 100 * rate  # Calculate expected based on live rate
        self.assertAlmostEqual(result, expected, places=2)
        self.print_output('USD', 'EUR', 100, expected, result)

    def test_eur_to_gbp(self):
        rate = self.converter.get_exchange_rate('EUR', 'GBP')
        result = self.converter.convert_currency('EUR', 'GBP', 50)
        expected = 50 * rate
        self.assertAlmostEqual(result, expected, places=2)
        self.print_output('EUR', 'GBP', 50, expected, result)

    # ... Add more test cases for different currency pairs

    def test_same_currency_conversion(self):
        rate = self.converter.get_exchange_rate('JPY', 'JPY')
        result = self.converter.convert_currency('JPY', 'JPY', 5000)
        expected = 5000 * rate
        self.assertAlmostEqual(result, expected, places=2)
        self.print_output('JPY', 'JPY', 5000, 5000, result)

    def test_zero_conversion(self):
        rate = self.converter.get_exchange_rate('USD', 'GBP')
        result = self.converter.convert_currency('USD', 'GBP', 0)
        expected = 0 * rate
        self.assertAlmostEqual(result, expected, places=2)
        self.print_output('USD', 'GBP', 0, 0, result)

    def test_invalid_currencies(self):
        with self.assertRaises(InvalidCurrencyError) as cm:
            self.converter.convert_currency('XYZ', 'ABC', 100)
        self.print_output('XYZ', 'ABC', 100, 'InvalidCurrencyError', str(cm.exception))

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError) as cm:
            self.converter.convert_currency('cm', 'USD', 'hello')
        self.print_output('cm', 'USD', 'hello', 'TypeError', str(cm.exception))


if __name__ == '__main__':
    unittest.main()