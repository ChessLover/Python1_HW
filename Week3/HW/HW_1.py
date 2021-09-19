import argparse
import datetime as dt

parser = argparse.ArgumentParser()

parser.add_argument("--num_y", help="Enter year.", type=int)
parser.add_argument("--num_d", help="Enter days.", type=int)

args = parser.parse_args()

current_date = dt.datetime.now()

print("Current date: ", current_date)
if args.num_y:
    print("Given years: ", args.num_y)
else: 
    args.num_y = 0
    print("Given years: not given")
    
if args.num_d:
    print("Given days: ", args.num_d)
else: 
    args.num_d = 0
    print("Given days: not given")


final_date = current_date + dt.timedelta(args.num_d + args.num_y*365)

print("Final date: ", final_date )