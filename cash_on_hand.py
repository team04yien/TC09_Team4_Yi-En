from pathlib import Path
import csv

# create a file path to csv file.
fp = Path.cwd()/"csv_reports"/"Cash_on_Hand.csv"
print(fp.exists())

# read the csv file 
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # Read the first data row to initialize previous_cash
    first_data_row = next(reader) 
    pervious_cash = float(first_data_row[1])

# Go through the rows, 
    for row in reader: 
        # name the according rows
        day = row[0] 
        cash_on_hand = float(row[1]) #float it as we need numberic operation
        current_cash = cash_on_hand
        difference = current_cash - pervious_cash  
        print (difference)
o


# # Initial first day to make it $0 
# pervious_cash_amount = row[0] 
# current_cash_amount = float(row[1]) 
# difference = current_cash_amount - pervious_cash_amount 