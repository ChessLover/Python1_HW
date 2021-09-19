import argparse

parser = argparse.ArgumentParser()

parser.add_argument("text", help="Enter any text.", type=str)

args = parser.parse_args()

if args.text: 
    print("The given string: ", args.text )
    print("All lowercase: ", args.text.lower() )
    print("All uppercase: ", args.text.upper() )