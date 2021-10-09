# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


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

''' Defining a general save_csv function that can be imported into other modules. 
Takes in 2 args, csvpath and data.  This will allow the user to pass filtered loan data 
and export to a *.csv file if desired.'''

def save_csv(csvpath, data, header=None):
    with open(csvpath, 'w', newline="") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=",")
        # Checks if a header is defined by the user before adding in raw data
        if header:
            csvwriter.writerow(header)
        # Iterates through the data by row and adds to the file to be exported.
        for row in data:
            csvwriter.writerow(row)

    