# The module 'argparse' can be used for making CLI apps using py
# EG:-  python main2.py -h

import argparse

class SingleLineFormatter(argparse.HelpFormatter):
    def _split_lines(self, text, width):
        # Prevent wrapping by keeping everything in one line
        return [text]

# Initialize parser with custom formatter
parser = argparse.ArgumentParser(formatter_class=SingleLineFormatter)

# Adding optional argument
parser.add_argument("-o", "--Output", help = "Show Output") # EG:-  python main2.py -o Blue
parser.add_argument("-add", "--Add", nargs="+", help = "Add integers and shows output") # 'nargs=+' allows to pass one or more arguments

# Read arguments from command line
args = parser.parse_args()

if args.Output:
    print(f"Displaying Output as: {args.Output}")

if args.Add:
    print("sum:", sum([int(i) for i in args.Add]))
