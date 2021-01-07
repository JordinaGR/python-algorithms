def cocktail(data):

    for i in range(len(data)-1):

        for j in range(len(data)-1, 0, -1):
            if data[j] < data[j-1]:
                data[j], data[j-1] = data[j-1], data[j]

        for k in range(len(data)-1):
            if data[k] > data[k+1]:
                data[k], data[k+1] = data[k+1], data[k]

    return data


data = [5, 2, 34, 3, 6, 4, 6, 4, 3, 64, 2, 3, 4]    
print(cocktail(data))