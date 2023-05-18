def find(disjoint, n):
    if disjoint[n] == -1:
        return n
    tmp = find(disjoint, disjoint[n])
    disjoint[n] = tmp
    return tmp

def join(disjoint, n1, n2):
    n1 = find(disjoint, n1)
    n2 = find(disjoint, n2)
    disjoint[n1] = n2

while True:
    n, m = map(int, input().split())
    if n == 0:
        break
    
    # Read in edges
    v = []
    for i in range(m):
        # Read in
        e = list(map(int, input().split()))

        # Make sure edges in correct format
        if e[0] > e[1]:
            e[0], e[1] = e[1], e[0]

        # Add
        v.append(e)

    # Sort edges by weight
    v.sort(key=lambda e: e[2])

    # Set up used node array
    disjoint = [-1] * n

    # Set up array of edges to keep and total weight
    keep = []
    weight = 0

    # Try to add each edge
    for i in v:
        # If they have the same parent, don't allow a cycle
        p1 = find(disjoint, i[0])
        p2 = find(disjoint, i[1])
        if p1 == p2:
            continue

        # Otherwise, add
        join(disjoint, i[0], i[1])
        weight += i[2]
        keep.append(i)

    # Make sure spanning tree is connected
    trees = disjoint.count(-1)
    if trees > 1:
        print("Impossible")
        continue

    # Print total weight
    print(weight)

    # Print all of the edges
    keep.sort(key=lambda e: (e[0], e[1]))
    for i in keep:
        print(i[0], i[1])