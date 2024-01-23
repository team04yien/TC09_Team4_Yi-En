# Team = Group 4 
# Members = Choy Yi En, Lim Yin Shan, Chan Jia Wei, Tan jia Heng 
# Student id = S10256100D, 
# Class number = TC09 


from pathlib import Path
import csv 

def analyze_cash_on_hand(filePaths) 
#combine the data from all the 3 CSV files for cash on hand 
total_cash_on_hand = 

# Paths to the CSV files
file_paths = [
    '/path/to/first/csv',
    '/path/to/second/csv',
    '/path/to/third/csv'
]

information = [] #create an empty list to append 
for filePath in filePaths:
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        data.append(list(csv_reader)) 

from pathlib import Path
import csv

def analyze_cash_on_hand(file_paths):
    # Combine the data from all the CSV files
    total_cash_on_hand = []
    for file_path in file_paths:
        with open(file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                # Convert 'Cash On Hand' from string to integer
                row['Cash On Hand'] = int(row['Cash On Hand'])
                total_cash_on_hand.append(row)
    
    # Sort the data by 'Day' to ensure the order (if needed)
    total_cash_on_hand.sort(key=lambda x: int(x['Day']))

    # Calculate the daily difference in Cash-on-Hand
    for i in range(1, len(total_cash_on_hand)):
        total_cash_on_hand[i]['Difference'] = total_cash_on_hand[i]['Cash On Hand'] - total_cash_on_hand[i-1]['Cash On Hand']
    total_cash_on_hand[0]['Difference'] = None  # First entry has no previous day

    # Analysis based on the trend of cash-on-hand (increment, decrement, fluctuation)
    # Your analysis code goes here...

# Paths to the CSV files
file_paths = [
    '/path/to/first/csv',
    '/path/to/second/csv',
    '/path/to/third/csv'
]

# Call the function
analyze_cash_on_hand(file_paths)
