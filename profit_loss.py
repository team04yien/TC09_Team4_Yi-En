from pathlib import Path
import csv

def check_list(list):
# function to loop through each item in list 
# to tell the overall trend in the series of cash_on_hand difference,
# inside this list, it can be either, always increasing, alwalys decreasing or fluctuating 
    """
    This function identifies the trend of the data set which can be increasing, decreasing or fluctuating
    One parameter required: A list where each inner list contains the day and the cash on hand difference for that day.
    
    """
    positive = 0  # Initialise positive and negative as 0
    negative = 0  
    for nested in list:  # nested is the elements in list 
        if nested[-1] > 0: # if the last element of the list is greater than 0, then is positive  
            positive += 1  # positive = 1  
        elif nested[-1] < 0:
            negative += 1  # count the total number of occurance 
    if positive and not negative:
        return  "always increasing"
    elif not positive and negative:
        return "always decreasing"
    elif positive and negative:
        return "fluctuating"
    
def always_positive(list):
    """
    This function identifies the day and amount of the highest increase in net profit, when the trend is always increasing
    One parameter required: A list where each inner list contains the day and the cash on hand difference for that day.
    """
    highest = 0 # set variable to zero 
    day = 0   # to rmb the day on which the highest value occurs 
    for nested in list:
        if nested[-1] > highest: # going down the list to find the highest value, if the value is higher than the highest, then it will be replaced to be the highest 
            highest = nested[-1]
            day = nested[0] # updates the day of the highest 
    return [day, highest]

def always_negative(list):
    """
    This function identifies the day and amount of the highest decrease in net profit, when the trend is always decreasing
    One parameter required: A list where each inner list contains the day and the cash on hand difference for that day.
    """
    lowest = 0
    day = 0
    for nested in list:
        if nested[-1] < lowest: # going down the list to find the lowest value, if the value is lower than the lowest, then it will be replaced to be the lowest 
            lowest = nested[-1]
            day = nested[0] # updates the day of the lowest
    return [day, lowest]

def fluctuate(list):
    """
    This function identifies all the deficit days and the top three highest deficits when the data is fluctuating
    One parameter required: A list where each inner list contains the day and the net profit difference for that day.
    """
    deficits = []    # create empty list to store days with deficits 
    to_sort = []    # list to sort deficits 
    for nested in list:
        if nested[-1] < 0:   # if negative number
            deficits.append(nested) # if yes, then add the nested number to the end of deficits list 
            to_sort.append([nested[-1], nested[0]])  # adding of decifics amount and day to the list to sort later 
        # putting deficit amount first, to sort, will sort the first element first to tell which the highest 
    to_sort.sort()    # to sort the data by ascending order by the deficit amount, to know the largest decifit amount 
    first = [to_sort[0][-1], to_sort[0][0]] # the first to_sort will be the largest (most negative) deficit amount, then put it into the new list
    second = [to_sort[1][-1], to_sort[1][0]] # Take the 2nd 
    third = [to_sort[2][-1], to_sort[2][0]]
    return deficits, first, second, third

def profit_loss_function():

    """
    This function combines the use of the functions listed above to processes net profit data from the profit and loss csv file, determind the trend of the data (increasing, decreasing, fluctuating), 
    and accordingly executes one of the 3 functions according to the trend and writes the results into the summary text file.

    No parameter needed
    """

    # Using the function with the file path
    fp = Path.cwd() / "csv_reports" / "Profit_and_Loss.csv"

    # read the csv file.
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header

        # create an empty list 
        data=[] 

        # append the 2 rows of net profit values into the data 
        for row in reader:
            data.append([row[0], row[-1]])  
    # create a empty list to store all the net profit difference values
    difference = []
    # variable prev_day is allocated to values in the first item in the first bracket in the list
    prev_day = data[0]
    # creating a for loop for all the days in the data list 
    for day in range(1, len(data)):
        profit_diff = int(data[day][-1]) - int(prev_day[-1]) # calculate the difference of net profit
        difference.append([data[day][0], profit_diff]) # append these difference values into the difference list 
        prev_day = [data[day][0], data[day][-1]] # allocating the previous day as the current day for the next cycle of the for loop

    # calling the check_list function to run the check on the difference datas in the difference list
    result = check_list(difference)

    #file path to txt file
    fp = Path.cwd()/"summary_report.txt"
    #creating txt file
    fp.touch()
    #opening the summary text file and set it to append mode
    with fp.open(mode="a", encoding="UTF-8", newline="") as file:

        # based on the result determined by the check_list function it will run either of the 3 codes based on the trend identified (increasing, decreasing and fluctuating trend) in the check_list function
        # if the trend of the net profit data is increasing then the always positive function would run and write the highest increase into the summary text file
        if result == "always increasing":
            highest = always_positive(difference)
            file.write(f'[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY\n[HIGHEST NET PROFIT SURPLUS] DAY {highest[0]}, AMOUNT: SGD{highest[-1]}')
            # if the trend of the net profit data is decreasing then the always negative function would run and write the highest deficit into the summary text file
        elif result == "always decreasing":
            lowest = always_negative(difference)
            file.write(f'[NET PROFIT DEFICIT] NET PROFIT EACH DAY IS LOWER THAN PREVIOUS DAY\n[HIGHEST PROFIT DECIFIT] DAY {lowest[0]}, AMOUNT: SGD{lowest[-1]*-1}')
            # if the trend of the net profit data is fluctuating then the fluctuate function would run and write all the deficits and also the top 3 deficits into the summary text file
        elif result == "fluctuating":
            deficits, first, second, third = fluctuate(difference)
            for deficit in deficits:
                file.write(f'\n[NET PROFIT DEFICIT] DAY {deficit[0]}, AMOUNT: SGD{deficit[-1]*-1}')
            file.write(f'\n[HIGHEST NET PROFIT DEFICIT] DAY {first[0]}, AMOUNT: SGD{first[-1]*-1}\n[2ND HIGHEST NET PROFIT DEFICIT] DAY {second[0]}, AMOUNT: SGD{second[-1]*-1}\n[3RD HIGHEST NET PROFIT DEFICIT] DAY {third[0]}, AMOUNT: SGD{third[-1]*-1}')