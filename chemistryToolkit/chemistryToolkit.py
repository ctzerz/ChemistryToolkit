# Chemistry Toolkit
# Main function
# Takes user input and return elemental properties

import csv
import elementSearch

cFilename = "Periodic Table of Elements.csv"

def readTable(filename):
    # Open the library of elements and save it as a list without the first
    # row
    with open(filename, newline = '') as csvfile:
        reader = csv.reader(csvfile)
        tableOfElements = list(reader)
        tableOfElements = tableOfElements[1:]
    return tableOfElements

def main():
    tableOfElements = readTable(cFilename)
    elementSearch.searchForElement(tableOfElements)

if __name__ == "__main__":
    main()