n, k = map(int, input().split())

events = []
for _ in range(n):
    s, e = map(int, input().split())
    events.append((s, e))
events.sort(key=lambda x: (x[1], x[0]))

ans = 0
endtime = set()
for i in range(n):
    it = next((x for x in endtime if x <= -events[i][0]), None)

    if it is None:
        if len(endtime) < k:
            endtime.add(-events[i][1] - 1)
            #ans += 1
        continue

    endtime.remove(it)
    endtime.add(-events[i][1] - 1)
    ans += 1

print(ans)