def read_input():
    while True:
        # read the input
        line = input().strip()
        # if it is empty, continue
        if line == "":
            continue
        #otherwise
        n, b = map(int, line.split())
        
        # end of the input
        if n == -1 and b == -1:
            break
        
        # read in the array
        arr = [int(input()) for _ in range(n)]
        yield n, b, arr

for n, b, arr in read_input():
    # we have to check the max of the array
    maxE = max(arr)
    low = 1
    high = maxE

    while low < high:
        mid = (low + high) // 2
        dist = sum((x + mid - 1) // mid for x in arr)

        if dist > b:
            low = mid + 1
        else:
            high = mid

    print(low)