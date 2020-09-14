def selection(data):

    for i in range(len(data)):
        minV = i

        for j in range(i, len(data)):
            if data[j] < data[minV]:
                minV = j

        data[minV], data[i] = data[i], data[minV] 

    return data

data = [3, 5, 1, 7, 4, 8, 6,4, 2, 6, 3, 7, 10, 53, 12]
print(selection(data))