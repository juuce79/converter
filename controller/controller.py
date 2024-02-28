from model.model import ConversionModel


class ConversionController:
    @staticmethod
    def handle_command_line_conversion(args):
        model = ConversionModel()  # Create a model instance

        if args.conversion_type:
            if args.conversion_type == '1':
                result = model.perform_currency_conversion(args.from_unit, args.to_unit, args.amount)
                if result:
                    print(f"{args.amount} {args.from_unit} is equal to {result} {args.to_unit}")
                else:
                    print("Conversion failed. Check if currencies are valid.")

            elif args.conversion_type == '2':
                result = model.perform_length_conversion(args.from_unit, args.to_unit, args.amount)
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
                model.handle_currency_conversion()

            elif choice == '2':
                model.handle_length_conversion()

            elif choice == '3':
                print("Exiting program...")
                break

            else:
                print("Invalid choice. Please try again.")
