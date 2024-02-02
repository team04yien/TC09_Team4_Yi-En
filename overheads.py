from pathlib import Path
import csv

def overhead_function():
    """
    This function runs through the overheads csv file and identifies the highest overhead category and percentage and writes the result into the summary text file
    No parameter needed
    """
    # create a file path to csv file.
    fp = Path.cwd()/"csv_reports"/"Overheads.csv"

    # read the csv file 
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header

    # create a list for total overheads 
        total_overheads = []

    # Go through the rows, 
        for row in reader: 
        # name the according rows
            category = row[0] 
            overhead = float(row[1]) #float it as we need numberic operation 

            total_overheads.append([category, overhead]) #append all the overhead categories and amounts into the total_overhead list

    #setting highest_overhead variable to 0
    highest_overhead = 0
    #setting the highest_overhead_category to an empty list
    highest_overhead_category = []
    # created a for loop for total_overheads where the loop runs through the overheads data and identifies the highest overhead category before stopping
    for category, overhead in total_overheads:
        if overhead > highest_overhead:
            highest_overhead = overhead
            highest_overhead_category = category

    #file path to txt file
    fp = Path.cwd()/"summary_report.txt"
    #creating txt file
    fp.touch()
    #opening the summary text file and set it to write mode
    with fp.open(mode="w", encoding="UTF-8", newline="") as file:
        #writing the highest overhead into the summary text file
        file.write(f"[HIGHEST OVERHEAD] {highest_overhead_category.upper()}: {highest_overhead}%")
