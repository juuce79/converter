import argparse
import sys

from controller.controller import ConversionController


def main():
    conversion_controller = ConversionController()  # Create a controller instance
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser(description="Choose conversion type and parameters.")
        parser.add_argument("conversion_type", choices=['1', '2'], help="1 for currency, 2 for length")
        parser.add_argument("--from", dest='from_unit',  help="Unit/currency to convert from")
        parser.add_argument("--to", dest='to_unit',  help="Unit/currency to convert to")
        parser.add_argument("--amount", type=float,  help="Amount to convert")

        args = parser.parse_args()

        conversion_controller.handle_command_line_conversion(args)
    else:
        conversion_controller.handle_interactive_mode()


if __name__ == "__main__":
    main()
