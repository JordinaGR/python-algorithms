import random

def random_sort(data):

    random.shuffle(data)
    for i in range(len(data)-1):
        if data[i] > data[i+1]:
            random_sort(data)

    return data

print(random_sort([3, 2, 1, 4]))