## import Path from pathlib into profit_loss.py
from pathlib import Path

## import the csv
import csv


## create a function for profit and loss
def pol_function():
    """
    this function will compute the difference in the net profit column if
    net profit on the current day is lower than that of the previous day
    if there is, the function will identify and write it in a summary.
    it is always higher, the function will return profit surplus.
    """

    ## create a file path for reading the profit and loss csv
    fp_read = Path.cwd() / "csv_reports" / "Profit and Loss.csv"
    ## create another file path for writing into the summary_report.txt
    fp_write = Path.cwd() / "summary_report.txt"

    ## create two lists, days and profit to store in the extracted data
    # from the profit and loss csv file.
    days = []
    profit = []

    ## open the fp_write file with .open() with mode,"r", to read the profit and loss
    # csv for data extraction
    with fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
        ## using .reader(), read the profit and loss csv file
        reader = csv.reader(file)
        next(reader)  # skip header

        ## create a for loop for the reader to append the data into the
        # respective lists.
        for row in reader:
            ## append the days in the csv in row[0] into the days list created
            ## as it is a value, convert the value to float for comparison
            days.append(float(row[0]))
            ## append the net profit in the csv in row[4] into the profit list created
            ## as it is a value, convert the value to float for comparison
            profit.append(float(row[4]))

    ## assign variable surplus as 1
    surplus = 1
    ## using len, assign the variable num_days with the number of days in the data
    num_days = len(days)
    ## create a range of days excluding 0 so that the code for loop would not be out
    # of range
    range_days = range(1, num_days)

    ## create a for loop for range_days to compare the profit for current day and
    # previous day
    for num in range_days:
        ## create a condition, using if to identify the days in which their net profit
        # is lesser than the previous day
        if profit[num] < profit[num - 1]:
            ## if condition applies, use operators to compute the difference of the identified days and assign
            # the differences into the variable, 'difference'
            difference = profit[num - 1] - profit[num]
            ## if condition is satisfied, surplus will be reassigned as 0
            surplus = 0
            ## open the fp_write file path with .open() with mode,"a", to append into
            # summary_report.txt
            with fp_write.open(mode="a", encoding="UTF8", newline="") as file:
                ## using .write(), append profit deficit with the identified day(s) and
                # difference(s)
                file.write(f"\n[PROFIT DEFICIT] DAY: {days[num]}, AMOUNT: USD{difference}")

    ## if there is each day is higher than the previous, surplus will remain = 1
    # condition if surplus equates to 1
    if surplus == 1:
        ## if condition is satisfied, use .open() with mode, "a", to append into
        # summary_report.txt
        with fp_write.open(mode="a", encoding="UTF8", newline="") as file:
            ## using .write(), append profit surplus with the following statement.
            file.write(f"\n[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
