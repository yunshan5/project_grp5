## import Path from pathlib into overheads.py
from pathlib import Path

## import the csv
import csv


def overheads_function():
    """
    the function will find the highest overhead category and generate the name
    of the expense along with the percentage
    """

    ## create a file path for reading the oh_value csv
    fp_read = Path.cwd() / "csv_reports" / "Overheads.csv"
    ## create another file path for writing into the summary_report.txt
    fp_write = Path.cwd() / "summary_report.txt"

    ## create two lists, expenses and oh_value
    expenses = []
    oh_value = []

    ## open the fp_write file with .open() with mode,"r", to read the overheads
    # csv for data extraction
    with fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
        ## using .reader(), read the overheads csv file
        reader = csv.reader(file)
        next(reader)  # skip header

        ## create a for loop for the reader to append the data into the
        # respective lists.
        for row in reader:
            ## append the name of expenses in the csv in row[0] into
            # the expenses list created
            expenses.append(row[0])
            ## append the overhead values in the csv in row[1] into
            # the oh_value list created
            ## as it is a value, convert the value to float for comparison
            oh_value.append(float(row[1]))

    ## using max() find the highest value in oh_value and assign it into 'highest_value'
    highest_value = max(oh_value)

    ## create a for loop for enumerate to loop the sequence and their value paring
    for num in enumerate(oh_value):
        ## create a condition, if the value in oh_value equates to the highest value
        if num[1] == highest_value:
            ## if the condition is satisfied, assign the name of expense paired with
            # the value into 'highest_exp'
            highest_exp = expenses[num[0]]
            ## then open the fp_write file path with .open() with mode,"w", to write and into
            # summary_report.txt
            ## since this is the first output, use the mode, "w", to overwrite the existing data
            # in the txt file.
            with fp_write.open(mode="w", encoding="UTF8", newline="") as file:
                ## using .write(), write the name of the expense with .upper() to full cap the name
                # with the identified, highest overhead value
                file.write(f"[HIGHEST OVERHEADS] {highest_exp.upper()}: {highest_value}%")
