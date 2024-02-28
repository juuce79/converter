from model.converters.convert_currency import CurrencyConverter
from model.converters.convert_length import LengthConverter


class ConversionModel:
    @staticmethod
    def perform_currency_conversion(from_currency, to_currency, amount):
        currency_converter = CurrencyConverter()  # Create converter when needed
        result = currency_converter.convert_currency(from_currency, to_currency, amount)
        return result

    @staticmethod
    def perform_length_conversion(from_unit, to_unit, value):
        length_converter = LengthConverter()
        result = length_converter.convert_length(from_unit, to_unit, value)
        return result

    def handle_currency_conversion(self):
        while True:
            from_currency = input("Enter currency to convert from (or type 'exit'): ").upper()
            if from_currency == "EXIT":
                break

            to_currency = input("Enter currency to convert to: ").upper()
            amount = float(input("Enter amount: "))

            result = self.perform_currency_conversion(from_currency, to_currency, amount)
            if result:
                print(f"{amount} {from_currency} is equal to {result} {to_currency}")
            else:
                print("Conversion failed. Check if currencies are valid.")

    def handle_length_conversion(self):
        while True:
            from_unit = input("Enter unit to convert from (or type 'exit'): ").lower()
            if from_unit == "exit":
                break

            to_unit = input("Enter unit to convert to: ").lower()
            value = float(input("Enter amount: "))

            result = self.perform_length_conversion(from_unit, to_unit, value)
            if result:
                rounded_result = self.round_to_nearest_nonzero(result)
                rounded_value = self.round_to_nearest_nonzero(value)
                print(f"{rounded_value} {from_unit} is equal to {rounded_result} {to_unit}")
            else:
                print("Conversion failed. Check if units are valid.")

    def handle_command_line_currency_conversion(self, args):
        result = self.perform_currency_conversion(args.from_unit, args.to_unit, args.amount)
        if result:
            print(f"{args.amount} {args.from_unit} is equal to {result} {args.to_unit}")
        else:
            print("Conversion failed. Check if currencies are valid.")

    def handle_command_line_length_conversion(self, args):
        result = self.perform_length_conversion(args.from_unit, args.to_unit, args.amount)
        if result:
            rounded_result = self.round_to_nearest_nonzero(result)
            rounded_value = self.round_to_nearest_nonzero(args.amount)
            print(f"{rounded_value} {args.from_unit} is equal to {rounded_result} {args.to_unit}")
        else:
            print("Conversion failed. Check if units are valid.")

    @staticmethod
    def currency_conversion_loop(currency_converter):
        while True:  # Conversion loop
            from_currency = input("Enter currency to convert from (or type 'exit'): ").upper()
            if from_currency == "EXIT":
                break

            to_currency = input("Enter currency to convert to: ").upper()
            amount = float(input("Enter amount: "))

            result = currency_converter.convert_currency(from_currency, to_currency, amount)
            if result:
                print(f"{amount} {from_currency} is equal to {result} {to_currency}")
            else:
                print("Conversion failed. Check if currencies are valid.")

    def length_conversion_loop(self, length_converter):
        while True:
            from_unit = input("Enter unit to convert from (or type 'exit'): ").lower()
            if from_unit == "exit":
                break

            to_unit = input("Enter unit to convert to: ").lower()
            value = float(input("Enter amount: "))

            result = length_converter.convert_length(from_unit, to_unit, value)
            if result:
                rounded_result = self.round_to_nearest_nonzero(result)  # Use model's rounding method
                rounded_value = self.round_to_nearest_nonzero(value)
                print(f"{rounded_value} {from_unit} is equal to {rounded_result} {to_unit}")
            else:
                print("Conversion failed. Check if units are valid.")

    @staticmethod
    def round_to_nearest_nonzero(number, max_decimal_places=12):
        """Rounds a number to a maximum number of decimal places and returns a string representation."""
        if number == 0:
            return "0"

        str_number = f"{number:.{max_decimal_places}f}"
        return str_number.rstrip("0").rstrip(".")
