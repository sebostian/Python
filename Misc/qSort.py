def qSort(data):
    if len(data) < 2:
        return data
    
    pivot = data[0]

    less = [i for i in data[1:] if i <= pivot]
    great = [i for i in data[1:] if i >pivot ]
                
    return qSort(less) + [pivot] + qSort(great) 
