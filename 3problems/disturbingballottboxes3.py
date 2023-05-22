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
c = 0
for N, B, arr in read_input():
    # we have to check the biggest city
    high = max(arr)
    low = 1
    #high = maxE
    
    while low < high:
        mid = (low + high) // 2 # integer division 
        dist = 0  # Initialize distribution variable
        for x in arr:  # Iterate over each element x in the arr list
            temp = x + mid - 1  # Calculate the value of (x + mid - 1)
            division_result = temp // mid  # Perform integer division of temp by mid
            dist += division_result  # Add the division_result to the dist variable
            # distribution now contains the sum of all the division results
        
        #print("mid", mid, "low", low, "high", high, "dist", dist)
        if dist > B:
            low = mid + 1 # binary search part. With +1 we ensure that the low never been the same value 
            #low = mid # binary search part
        else:
            high = mid
        c += 1
    print(low)
    #print(c)