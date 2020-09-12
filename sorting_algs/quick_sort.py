data = [8,6,7,9,4,5,2,1,3]

def main(data):
    if len(data) <= 1:
        return data
    else:
        num = data.pop()
    left = []
    right = []

    for i in data:
        if i > num:
            right.append(i)
        else:
            left.append(i)
    return main(left) + [num] + main(right)

print(main(data))



