from sys import argv

n = 100

with open(argv[1], 'w') as file:
    file.write(str(n))
    file.write('\n')
    print(n)

    for i in range(n):
        if i == 0:
            file.write(str(i)+':100000:V:')
            file.write('\n')
            print(str(i)+':100000:V:')
            continue
        file.write(str(i)+':100000:V:'+str(i-1))
        file.write('\n')
        print(str(i)+':100000:V:'+str(i-1))
