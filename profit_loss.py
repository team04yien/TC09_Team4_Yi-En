from pathlib import Path
import csv

# create a file path to csv file.
fp = Path.cwd()/"csv_reports"/"Profit_and_Loss.csv"
print(fp.exists())