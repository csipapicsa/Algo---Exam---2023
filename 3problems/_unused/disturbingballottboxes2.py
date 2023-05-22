def read_input():
    while True:
        # read the input
        line = input().strip()
        # if it is empty, continue
        if line == "":
            continue
        #otherwise
        N, B = map(int, line.split())
        
        # end of the input
        if N == -1 and B == -1:
            break
        
        # read in the array
        arr = [int(input()) for _ in range(N)]
        yield N, B, arr

for N, B, arr in read_input():
    # we have to check the max of the array
    maxE = max(arr)
    low = 1
    #low = min(arr)
    high = maxE

    while low < high:
        #print("mid", mid, "low", low, "high", high)
        mid = (low + high) // 2
        dist = sum((x + mid - 1) // mid for x in arr)
        print("dist", dist)
        print("mid", mid, "low", low, "high", high, "dist", dist)
        if dist > B:
            low = mid + 1
        else:
            high = mid

    print(low)