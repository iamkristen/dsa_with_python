def oddnumber(maxNum):
    data = []
    for i in range(maxNum):
        if(i %2 != 0):
            data.append(i)
    return data

print(oddnumber(20))