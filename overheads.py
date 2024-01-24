from pathlib import Path
import csv

# create a file path to csv file.
fp = Path.cwd()/"csv_reports"/"Overheads.csv"
print(fp.exists())

# read the csv file 
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header


# Go through variables to track the category with the highest overhead
    highest_overhead_amount = -1 # to ensure that all overhead amount get runs through as all is bigger than -1

# Go through the rows, 
    for row in reader: 
        # name the according rows
        category = row[0] 
        overhead = float(row[1]) #float it as we need numberic operation 

    # Check if overhead is greater than the highest recorded overhead
        if overhead > highest_overhead_amount:
            highest_overhead_category = category
            highest_overhead_amount = overhead

# Print category with highest overhead
print(f"Category with the highest overhead is '{highest_overhead_category}' with Total overhead amount of ${highest_overhead_amount:.2f}.") 