# import sys

# Uncomment the following line to read from a file
# sys.stdin = open('in.txt', 'r')

while True:
    inp = input()
    if len(inp):
        print("there is nothing")
    else:
        n, b = map(int, inp.split())
        if n == -1 and b == -1:
            break
            
        arr = []
        for _ in range(n):
            arr.append(int(input()))
        #arr = list(map(int, input().split()))
        maxE = max(arr)

        low = 1
        high = maxE
        print(arr)
        while low < high:
            mid = (low + high) // 2
            dist = sum((x + mid - 1) // mid for x in arr)

            if dist > b:
                low = mid + 1
            else:
                high = mid
        print(low)