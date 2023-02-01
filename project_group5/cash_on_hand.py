## import Path from pathlib into cash_on_hand.py
from pathlib import Path

## import the csv
import csv


## create a function for cash on hand
def coh_function():
    """
    this function will compute the different in the cash on hand if cash on hand
    on the current day is lower than that of the previous day.
    if there is, the function will identify and write it in the summary.
    it is always higher, the function will return cash surplus.
    """

    ## create a file path for reading the cash on hand
    fp_read = Path.cwd() / "csv_reports" / "Cash on Hand.csv"
    ## create another file path for writing into summary_report.txt
    fp_write = Path.cwd() / "summary_report.txt"

    ## create two lists, cash and days to store in the extracted data from
    # cash on hand csv file.
    cash = []
    days = []

    ## open the fp_write file with .open() with mode,"r", to read the cash on hand
    # csv for data extraction
    with fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
        ## using .reader(), read the cash on hand csv file
        reader = csv.reader(file)
        next(reader)  # skip header

        ## create a for loop for the reader to append the data into the
        # respective lists.
        for row in reader:
            ## append the cash on hand in the csv in row[1] into the cash list created
            ## as it is a value, convert the value to float for comparison
            cash.append(float(row[1]))
            ## append the days in the csv in row[0] into the days list created
            ## as it is a value, convert the value to float for comparison
            days.append(float(row[0]))

    ## assign variable surplus as 1
    surplus = 1
    ## using len, assign the variable num_days with the number of days in the data
    num_days = len(days)
    ## create a range of days excluding 0 so that the code for loop would not be out
    # of range
    range_days = range(1, num_days)

    ## create a for loop for range_days to compare the cash on hand for current day and
    # previous day
    for num in range_days:
        ## create a condition, using if to identify the days in which their cash on
        # is lesser than the previous day
        if cash[num] < cash[num - 1]:
            ## if condition applies use operators to compute the difference of the identified days and assign
            # the differences into the variable, 'difference'
            difference = cash[num - 1] - cash[num]
            ## if condition is satisfied, surplus will be reassigned as 0
            surplus = 0
            ## open the fp_write file path with .open() with mode,"a", to append into
            # summary_report.txt
            with fp_write.open(mode="a", encoding="UTF8", newline="") as file:
                ## using .write(), append cash deficit with the identified day(s) and
                # difference(s)
                file.write(f"\n[CASH DEFICIT] DAY: {days[num]}, AMOUNT: USD{difference}")

    ## if there is each day is higher than the previous, surplus will remain = 1
    # condition if surplus equates to 1
    if surplus == 1:
        ## if condition is satisfied, use .open() with mode, "a", to append into
        # summary_report.txt
        with fp_write.open(mode="a", encoding="UTF8", newline="") as file:
            ## using .write(), append cash surplus with the following statement.
            file.write(f"\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
