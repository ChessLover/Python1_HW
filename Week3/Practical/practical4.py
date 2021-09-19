import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--age", help="Enter your age.", type=int, default=7)

args = parser.parse_args()

if args.age: 
    print("Happy Birthday, you are already %d years old!" % args.age)