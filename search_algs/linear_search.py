def linear(data, n):

    for i, item in enumerate(data):
        if item == n:
            print(f'{n} is in position {i}')
    return None

data = [4,3,1,5,6,7,8,4,3,5,7,6,8,9,6,4,3,5,2,1,33,5,6,76,8,7,5]
linear(data, 9)