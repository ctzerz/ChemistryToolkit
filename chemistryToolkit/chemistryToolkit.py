# Chemistry Toolkit
# Main function
# Takes user input and return elemental properties

import csv

cElementNumberIndex = 0
cElementNameIndex   = 1
cElementSymbolIndex = 2
cElementMassIndex   = 3

# Open the library of elements and save it as a list without the first
# row
with open('Periodic Table of Elements.csv', newline = '') as csvfile:
    reader = csv.reader(csvfile)
    tableOfElements = list(reader)
    tableOfElements = tableOfElements[1:]
        
# Get desired element from user
userElement = input("Enter an element number, name or symbol: ")

def elementIndex(data, query):
    for subList in data:
        if (query == subList[cElementNumberIndex]
        or query.lower() == subList[cElementNameIndex].lower()
        or query.lower() == subList[cElementSymbolIndex].lower()):
            return data.index(subList)
    raise ValueError("'{query}' is not in the table")

tableRow = elementIndex(tableOfElements, userElement)

print("Element:      ",tableOfElements[tableRow][cElementNameIndex])
print("Atomic Number:",tableOfElements[tableRow][cElementNumberIndex])
print("Atomic Mass:  ",tableOfElements[tableRow][cElementMassIndex])

input("Press Enter to continue...")
