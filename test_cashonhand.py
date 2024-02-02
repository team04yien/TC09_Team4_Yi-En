from pathlib import Path
import csv

def check_list(list):
# function to loop through each item in list (for loop)
# to tell the overall trend in the series of cash_on_hand difference,
# inside this list, it can be either, always increasing, alwalys decreasing or fluctuating 
    """

    """
    positive = 0 #boolean variables , True is a value of 1, False is a value of 0  (0)
    negative = 0  #Initialise positive and negative as 0, need to use later in the code, of don't have this code then there would be an error 
    for nested in list:  # nested is the elements in list 
        if nested[-1] > 0: # if the last element of the list is greater than 0, then is positive  
            positive += 1  # adds right to left then assign back to left, so positive = 1  
        elif nested[-1] < 0:
            negative += 1  # += 1 is meant to count the total number of occurance 
    if positive and not negative:
        return "always increasing" 
    elif not positive and negative:
        return "always decreasing" 
    elif positive and negative:
        return "fluctuating" 
    
def always_positive(list):
    """
    
    """
    highest = 0     #highest, set variable to zero 
    day = 0         # to rmb the day on which the highest value occurs 
    for nested in list:
        if nested[-1] > highest:  # going down the list to find the highest value, if the value is higher than the highest, then it will be replaced and be the highest 
            highest = nested[-1]
            day = nested[0] # updates the day of the highest 
    return [day, highest] 

def always_negative(list):
    lowest = 0
    day = 0
    for nested in list:
        if nested[-1] < lowest:
            lowest = nested[-1]
            day = nested[0]
    return [day, lowest]

def fluctuate(list):
    deficits = []    # create empty list to store days with deficits 
    to_sort = []    # list to sort deficits 
    for nested in list:
        if nested[-1] < 0:   # if it is a negative number
            deficits.append(nested) # if yes, then add the nested number to the end of deficits list 
            to_sort.append([nested[-1], nested[0]])  # adding of decifics amount and day to the list to sort later 
        # we put the deficit amount first as later the to sort, will sort the first element, then by this can tell which the highest 
    to_sort.sort()    # to sort the data by ascending order by the deficit amount, to know the largest decifit amount 
    first = [to_sort[0][-1], to_sort[0][0]] # the first to_sort will be the largest (most negative) deficit amount, then put it into the new list
    second = [to_sort[1][-1], to_sort[1][0]] # Take the 2nd 
    third = [to_sort[2][-1], to_sort[2][0]]
    return deficits, first, second, third


# Gobal scope is outside the function, so it will be the same through out, but once the variable is inside a local scope, the variable will not be able to run after the print, it does not exist anymore.   
def cash_on_hand_function():
    """
    
    """

    # Using the function with the file path
    fp = Path.cwd() / "csv_reports" / "Cash_on_Hand.csv"

    # read the csv file.
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header

        # create an empty list 
        data=[] 

        # append 
        for row in reader:
            data.append([row[0], row[-1]])  
    
    difference = []
    prev_day = data[0]

    for day in range(1, len(data)):
        profit_diff = int(data[day][-1]) - int(prev_day[-1])
        difference.append([data[day][0], profit_diff])
        prev_day = [data[day][0], data[day][-1]]

    result = check_list(difference)

    #file path to txt file
    fp = Path.cwd()/"summary_report.txt"
    #creating txt file
    fp.touch()
    #opening the summary text file and set it to write mode
    with fp.open(mode="a", encoding="UTF-8", newline="") as file:

        if result == "always increasing":
            highest = always_positive(difference)
            file.write(f'[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN PREVIOUS DAY\n[HIGHEST CASH SURPLUS] DAY {highest[0]}, AMOUNT: SGD{highest[-1]}')
        elif result == "always decreasing":
            lowest = always_negative(difference)
            file.write(f'[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN PREVIOUS DAY\n[HIGHEST CASH DECIFIT] DAY {lowest[0]}, AMOUNT: SGD{lowest[-1]*-1}')
        elif result == "fluctuating": 
            deficits, first, second, third = fluctuate(difference)
            for deficit in deficits:
                file.write(f'\n[CASH DEFICIT] DAY {deficit[0]}, AMOUNT: SGD{deficit[-1]*-1}')
            file.write(f'\n[HIGHEST CASH DEFICIT] DAY {first[0]}, AMOUNT: SGD{first[-1]*-1}\n[2ND HIGHEST CASH DEFICIT] DAY {second[0]}, AMOUNT: SGD{second[-1]*-1}\n[3RD HIGHEST CASH DEFICIT] DAY {third[0]}, AMOUNT: SGD{third[-1]*-1}')