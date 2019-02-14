def checkSumIsValid(data, checkSum):
    return getCheckSum(data) == checkSum

def getCheckSum(data):
    checkSum = 1
    for i in range(0, len(data)):
        for j in range(i+1, len(data)):
            sum = data[i] + data[j]
            if (sum % 3 == 1 and sum > checkSum):
                checkSum = sum
    print(checkSum)          
    return checkSum
