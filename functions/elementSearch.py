# Element Search
# Search for an element and print out properties

#import columnIndices

ElementNumber = 0
ElementName   = 1
ElementSymbol = 2
ElementMass   = 3

class ElementSearch:
    def elementIndex(data, query):
        for subList in data:
            #if (query == subList[columnIndices.ElementNumber]
            #or query.lower() == subList[columnIndices.ElementName].lower()
            #or query.lower() == subList[columnIndices.ElementSymbol].lower()):
            if (query == subList[ElementNumber]
            or query.lower() == subList[ElementName].lower()
            or query.lower() == subList[ElementSymbol].lower()):
                return data.index(subList)
        raise ValueError("'{query}' is not in the table")
    
    def elementNumber(data, index):
        return data[index][ElementNumber]
    
    def elementName(data, index):
        return data[index][ElementName]
    
    def elementSymbol(data, index):
        return data[index][ElementSymbol]

    #def searchForElement(table, userElement):
        # Get desired element from user
        #userElement = input("Enter an element number, name or symbol: ")

        #tableRow = elementIndex(table, userElement)

        #print("Element:      ",table[tableRow][columnIndices.ElementName])
        #print("Atomic Number:",table[tableRow][columnIndices.ElementNumber])
        #print("Atomic Mass:  ",table[tableRow][columnIndices.ElementMass])

        #input("Press Enter to continue...")

        #return tableRow
