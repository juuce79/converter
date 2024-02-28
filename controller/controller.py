from model.model import ConversionModel
from model.converters.convert_currency import CurrencyConverter
from model.converters.convert_length import LengthConverter


class ConversionController:
    @staticmethod
    def handle_command_line_conversion(args):
        model = ConversionModel()  # Create a model instance

        if args.conversion_type:
            if args.conversion_type == '1':
                currency_converter = CurrencyConverter()
                result = currency_converter.convert_currency(args.from_unit, args.to_unit, args.amount)
                if result:
                    print(f"{args.amount} {args.from_unit} is equal to {result} {args.to_unit}")
                else:
                    print("Conversion failed. Check if currencies are valid.")

            elif args.conversion_type == '2':
                length_converter = LengthConverter()
                result = length_converter.convert_length(args.from_unit, args.to_unit, args.amount)
                if result:
                    rounded_result = model.round_to_nearest_nonzero(result)
                    rounded_value = model.round_to_nearest_nonzero(args.amount)
                    print(f"{rounded_value} {args.from_unit} is equal to {rounded_result} {args.to_unit}")
                else:
                    print("Conversion failed. Check if units are valid.")

    @staticmethod
    def handle_interactive_mode():
        model = ConversionModel()  # Create a model instance

        while True:
            choice = input("Choose conversion type (1: Currency, 2: Length, 3: Exit): ")

            if choice == '1':
                currency_converter = CurrencyConverter()
                model.currency_conversion_loop(currency_converter)

            elif choice == '2':
                length_converter = LengthConverter()
                model.length_conversion_loop(length_converter)

            elif choice == '3':
                print("Exiting program...")
                break

            else:
                print("Invalid choice. Please try again.")