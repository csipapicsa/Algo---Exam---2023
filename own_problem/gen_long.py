n = 10000

print(n)

for i in range(n):
    if i == 0:
        print(str(i)+':100000:V:')
        continue
    print(str(i)+':100000:V:'+str(i-1))

print(str(int((n*100000)/1.5683754)))