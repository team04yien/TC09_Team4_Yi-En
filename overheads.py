from pathlib import Path
import csv

# create a file path to csv file.
fp = Path.cwd()/"csv_reports"/"Overheads.csv"
print(fp.exists())

# read the csv file 
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

# create a dictionary for total overheads 
    total_overheads = {} 

# Go through the rows, 
    for row in reader: 
        # name the according rows
        category = row[0] 
        overhead = float(row[1]) #float it as we need numberic operation 

# sum up overheads by category 
        if category in total_overheads:
            # if category is in total_overheads, add overhead into existing amount 
            total_overheads[category] += overhead 
        else:
            #else, create a new overhead
            total_overheads[category] = overhead 
        
print (total_overheads)
  