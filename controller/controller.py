from model.model import ConversionModel


class ConversionController:

    @staticmethod
    def handle_command_line_mode(args):
        model = ConversionModel()

        if args.conversion_type:
            if args.conversion_type == '1':
                model.handle_command_line_currency_conversion(args)

            elif args.conversion_type == '2':
                model.handle_command_line_length_conversion(args)

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
