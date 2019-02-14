def func(data):
    if len(data) == 0:
        return 0
    return data[0] + func(data[1:])

    
def funcMax(data):
    if len(data) == 2:
        return data[0] if data[0] > data[1] else data[1]
    
    max = funcMax(data[1:]) 
    return data[0] if data[0] > max else max

