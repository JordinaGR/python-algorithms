def binary(data, n):

    while not (len(data) == 0 or (len(data) == 1 and data[0] != n)):

        mid = data[len(data) // 2]

        if mid == n:
            return True
            break

        if mid > n:
            data = data[:len(data) // 2]
            
        elif mid < n:
            data = data[len(data) // 2 + 1:]

    return False

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary(data, 0))
