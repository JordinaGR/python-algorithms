def shellSort(data): 
  
    n = len(data) 
    gap = n//2

    while gap > 0: 
  
        for i in range(gap,n): 

            temp = data[i] 
            j = i 

            while  j >= gap and data[j-gap] >temp: 
                data[j] = data[j-gap] 
                j -= gap 

            data[j] = temp 
        gap //= 2
    
    return data

data = [4, 3, 6, 4, 1, 2, 4, 5, 6, 23, 1, 3]

print(shellSort(data))
