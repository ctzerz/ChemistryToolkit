# Chemistry Toolkit
# Main function
# Takes user input and return elemental properties

import csv

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
        if query == subList[0] or query == subList[1] or query == subList[2]:
            return data.index(subList)
    raise ValueError("'{query}' is not in the table")

tableRow = elementIndex(tableOfElements, userElement)

print("Element:",tableOfElements[tableRow][1])
print("Atomic Number:",tableOfElements[tableRow][0])
print("Atomic Mass:",tableOfElements[tableRow][2])

input("Press Enter to continue...")
