import argparse

parser = argparse.ArgumentParser()

parser.add_argument("text", help="Enter any text.", type=str)
parser.add_argument("first_word", help="Enter any word from the text.", type=str)
parser.add_argument("second_word", help="Enter any word you want to replace with.", type=str)

args = parser.parse_args()

print("The given text: ", args.text)
print("First word: ", args.first_word)
print("Second word: ", args.second_word)

new_string = args.text.replace(args.first_word, args.second_word)

print("Output string: ", new_string)