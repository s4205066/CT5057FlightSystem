import pandas as pd


def bubbleSort(list):
    newArray = list
    for i in range(len(newArray)-1, 0, -1):
        swapped=False
        for j in range(i):
            if newArray[j] > newArray[j+1]:
                temp = newArray[j]
                newArray[j] = newArray[j+1]
                newArray[j+1] = temp
                #print("Swapped element " + str(j) + " with element " + str(j+1))
                swapped=True
        if not swapped:
            #print("Not Swapped")
            break

    return newArray    

def binarySearchDF(DF, searchColumn, searchValue):
    lowIdx = 0
    midIdx = 0
    hiIdx = DF.shape[0] -1
    print(hiIdx)

    #print(DF.columns)
    sortedList = bubbleSort(DF[searchColumn].tolist())
    print("sortedList: " + str(sortedList))
    while lowIdx<=hiIdx:
        midIdx = (hiIdx + lowIdx) // 2
        if sortedList[midIdx] < searchValue:
            #target is larger than midIdx
            lowIdx = midIdx+1
        elif sortedList[midIdx] > searchValue:
            hiIdx = midIdx-1
        else:
            print("Item " + str(searchValue) + " found at index: " + str(midIdx))
            return sortedList[midIdx]

    #If target NOT in sortedList
    print("Target " + str(searchValue) + " is not in searchList")

if __name__ == "__main__":
    #df = pd.read_csv("flights.csv")
    #column = "Price"
    #target = 12346
    #binarySearchDF(df, column, target)

    binarySearchDF(pd.read_csv("tickets.csv"), "Name", "dhfd")
    
#     testArr = [8,1,56,8,17,2,6,0,2,48, 14, 86, 98, 24, 82, 50, 12,45]
#     print(testArr)
#     newArr = bubbleSortNum(testArr)
#     print(newArr)
#     resultItem = binarySearchNum(newArr, 17)
#     print("Search item found: " + str(resultItem))