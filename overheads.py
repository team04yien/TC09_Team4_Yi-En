from pathlib import Path
import csv

# create a file path to csv file.
fp = Path.cwd()/"csv_reports"/"Overheads.csv"
print(fp.exists())

# read the csv file 
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

# Go through the rows, 
    for row in reader: 
        # name the according rows
        category = row[0] 
        overhead = float(row[1]) #float it as we need numberic operation 

# create a dictionary for total overheads
        total_overheads = float({}) #float everything in the dictionary 

# sum up overheads by category 
        
        
 
 
    # # create an empty list for overheads record
    # overheadsRecords = [] 

    # # append overhead record into the overheadRecords list
    # for row in reader:
    #     category = row[0]
    #     overhead = float(row[1])  # Convert overhead to float for numerical operations
    #     overheadsRecords.append([category, overhead])    