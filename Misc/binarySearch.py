def binarySearch(data, item):
    low = 0
    high = len(data)-1
    while (low <= high):
        mid = (low + high) // 2
        guess = data[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid -1
        else:
            low = mid + 1
    return None

        
            
        
    
