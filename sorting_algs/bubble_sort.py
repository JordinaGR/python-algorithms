data = [8,7,9,5,6,3,2,4,1]

for _ in range(len(data)-1):
    for i in range(len(data)-1):
        if data[i] > data[i+1]:
            data[i], data[i+1] = data[i+1], data[i]

print(data)