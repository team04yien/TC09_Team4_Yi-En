from pathlib import Path
import csv

# create a file path to csv file.
fp = Path.cwd()/"csv_reports"/"Cash_on_Hand.csv"
print(fp.exists())

# Create an empty list for deficits to append later 
deficits = []  

# read the csv file 
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # Read the first data row to initialize previous_cash
    first_data_row = next(reader) 
    previous_cash = float(first_data_row[1])

# Go through the rows, 
    for row in reader: 
        # name the according rows
        day = row[0] 
        cash_on_hand = float(row[1]) #float it as we need numberic operation
        current_cash = cash_on_hand
        difference = current_cash - previous_cash 
        previous_cash = current_cash # the pervious cash was initially set as the first collum, reset it after running every rounds of loops, that current cash becomes pervious cash  
        print (difference)

# # checking for deficits 
#         if difference <  0:
#             # Record the deficit (store the day and the absolute value of the deficit)
#             deficits.append([day, difference]) 
#             print (deficits)