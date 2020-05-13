def insertion(data):
    k = 0
    for i in range(len(data) - 1):
        if data[k] > data[k + 1]:
            data[k], data[k + 1] = data[k + 1], data[k]

            k += 1
            for j in range(len(data[:k])):
                k = 0
                if data[k] > data[k + 1]:
                    data[k], data[k + 1] = data[k + 1], data[k]

                    k += 1
                else:
                    k += 1
                    return insertion(data)
        else:
            k += 1


    print(data)

data = [4, 2, 3, 1, 5, 2, 5, 6, 7, 3, 5, 7, 8, 4]
insertion(data)
