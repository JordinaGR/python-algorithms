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

data = [2, 3, 4, 1, 5]
insertion(data)
