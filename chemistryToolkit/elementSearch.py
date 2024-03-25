# Element Search
# Search for an element and print out properties

import columnIndices

def elementIndex(data, query):
    for subList in data:
        if (query == subList[columnIndices.ElementNumber]
        or query.lower() == subList[columnIndices.ElementName].lower()
        or query.lower() == subList[columnIndices.ElementSymbol].lower()):
            return data.index(subList)
    raise ValueError("'{query}' is not in the table")

def searchForElement(table):
  # Get desired element from user
  userElement = input("Enter an element number, name or symbol: ")

  tableRow = elementIndex(table, userElement)

  print("Element:      ",table[tableRow][columnIndices.ElementName])
  print("Atomic Number:",table[tableRow][columnIndices.ElementNumber])
  print("Atomic Mass:  ",table[tableRow][columnIndices.ElementMass])

  input("Press Enter to continue...")
