def binary(data, n):
    if len(data) == 0 or (len(data) == 1 and data[0] != n):
        return False

    mid = data[len(data) // 2]


    if mid == n: return True
    if mid > n: return binary(data[:len(data) // 2], n)
    if mid < n: return binary(data[len(data) // 2 + 1:], n)


data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary(data, 4))
