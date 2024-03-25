# Chemistry Toolkit
# Main function
# Takes user input and return elemental properties

import csv
import elementSearch

# Open the library of elements and save it as a list without the first
# row
with open('Periodic Table of Elements.csv', newline = '') as csvfile:
    reader = csv.reader(csvfile)
    tableOfElements = list(reader)
    tableOfElements = tableOfElements[1:]
        
elementSearch.searchForElement(tableOfElements)