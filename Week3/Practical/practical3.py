import argparse

parser = argparse.ArgumentParser()

parser.add_argument("name", help="Enter your name.", type=str)

args = parser.parse_args()

if args.name: 
    print("Welcome, %s!" % args.name)