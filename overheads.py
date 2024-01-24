from pathlib import Path
import csv

# create a file path to csv file.
fp = Path.cwd()/"csv_reports"/"Overheads.csv"
print(fp.exists())

# read the csv file 
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty list for overheads record
    overheadsRecords = [] 

    # append overhead record into the overheadRecords list
    for row in reader:
        category = row[0]
        overhead = float(row[1])  # Convert overhead to float for numerical operations
        overheadsRecords.append([category, overhead])   