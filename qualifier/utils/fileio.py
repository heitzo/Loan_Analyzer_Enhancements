# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
header = ["Lender", "Max Loan Amount", 'Max LTV', 'Max DTI', 'Min Credit Score', 'Interest Rate']

def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

# function that saves data to a csv file
def save_csv(csvpath, data, header = None):
    #open csv writer
    with open(csvpath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=",")
        #if there is a header then the csvwriter will input as header
        if header:
            csvwriter.writerow(header)
            # write data to csv file
        csvwriter.writerows(data)
        #let the customer know the process is working
    print("Writing qualified loan data to csv file...")
