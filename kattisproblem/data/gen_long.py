#! /usr/env/python3

from sys import argv
import random

n = int(argv[1])
lengths = int(argv[2])
num_test_cases = int(argv[3])

random.seed(int(argv[4]))

print(n)

for i in range(n):
    if i == 0:
        print(str(i)+':'+ str(lengths) + ':V:')
        continue

    print(str(i)+':'+ str(lengths) + ':V:'+str(i-1))

for _ in range(num_test_cases):
    print(random.randint(1, lengths * n))


