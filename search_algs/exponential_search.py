
def binary_search(data, head, tail, val):
    if tail >= head:
        mid = (head+tail) // 2

        if data[mid] == val:
            return True

        elif data[mid] < val:
            return binary_search(data, mid+1, tail, val)

        elif data[mid] > val:
            return binary_search(data, head, mid-1, val)

    return False

def exponential(data, val):
    if data[0] == val:
        return True

    i = 1
    n = len(data)
    while i < n and data[i] <= val:
        i = i*2

    return binary_search(data, i//2, min(i, n-1), val)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
val = 3
print(exponential(data, val))
