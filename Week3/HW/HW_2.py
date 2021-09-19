import argparse
parser = argparse.ArgumentParser()

parser.add_argument("text", help="Enter any text.", type=str)
args = parser.parse_args()

if (len(args.text) >= 7) and ( len(args.text) % 2 == 1) : 
    print("Text has more than 7 characters and number is odd.")
    
    middle_char_id = len(args.text)//2 + 1
    new_string = args.text[:(middle_char_id-2)] + args.text[(middle_char_id-2):(middle_char_id+1)].upper() + args.text[(middle_char_id+1):]
    
    print("The old string: ", args.text)
    print("Middle 3 caracters are: ", args.text[(middle_char_id-2):(middle_char_id+1)])
    print("The new string: ", new_string)
     
else: 
    print("String is not valid for this problem.")