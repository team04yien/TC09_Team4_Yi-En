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
            total_overheads[category] += overhead
        else:
            total_overheads[category] = overhead 
        


print (f"")
        
 
 
    # # create an empty list for overheads record
    # overheadsRecords = [] 

    # # append overhead record into the overheadRecords list
    # for row in reader:
    #     category = row[0]
    #     overhead = float(row[1])  # Convert overhead to float for numerical operations
    #     overheadsRecords.append([category, overhead])    