def countingSort(data):
    mval = max(data)

    buckets = [0 for i in range(mval + 1)]

    for i in data:
        buckets[i] += 1

    i = 0
    for j in range(mval + 1):
        for _ in range(buckets[j]):
            data[i] = j
            i += 1

    return data

x = countingSort([1,2, 1, 3, 5, 3, 4, 6, 1, 23, 5, 4, 65, 1, 2, 3, 4])
print(x)
