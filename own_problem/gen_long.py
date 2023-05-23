from sys import argv

n = int(argv[1])
lengths = int{argv[2]}
num_test_cases = int(argv[3])

print(n)

for i in range(n):
    if i == 0:
        print(str(i)+':'+ str(lengths) + ':V:')
        continue

    print(str(i)+':'+ str(lengths) + ':V:'+str(i-1))


