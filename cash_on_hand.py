from pathlib import Path
import csv

# create a file path to csv file.
fp = Path.cwd()/"csv_reports"/"Cash_on_Hand.csv"
print(fp.exists())

