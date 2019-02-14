def selectSort(data):
    result = []
    for i in range(0, len(data)):        
        minIndex = getMin(data)
        minItem = data.pop(minIndex)
        result.append(minItem)
    return result

def getMin(data):
    minIndex = 0
    for i in range(1, len(data)):
        if data[i] < data[minIndex]:
            minIndex = i
    return minIndex
