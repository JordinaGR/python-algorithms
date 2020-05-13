def binary(data, n):
    if len(data) == 0 or (len(data) == 1 and data[0] != n):
        print('not here')

    try:
        mid = data[len(data) // 2]
    except:
        print('Error, try again')
        quit()

    if mid == n: print('Found it', n)
    if mid > n: return binary(data[:len(data) // 2], n)
    if mid < n: return binary(data[len(data) // 2 + 1:], n)


data = [-4, -2, -1, 1, 2, 3.5, 4, 5, 6, 7]
binary(data, 8)
