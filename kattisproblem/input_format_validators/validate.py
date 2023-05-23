#! /usr/env/python3
import sys

n = int(input())
assert 0 < n <= 100000

for _ in range(n):
    info = input().split(':')

    name = int(info[0].strip())
    time = int(info[1].strip())
    variability = info[2].strip()
    dependencies_str = info[3].strip()

    assert 0 <= name < n
    assert 0 <= time <= 1000000
    assert variability in {'V', 'C'}
    if dependencies_str:
        for string in dependencies_str.strip().split(' '):
            int_ = int(string)
            assert 0 <= int_ < n

count = 0
while True:
    try:
        test_case = int(input().strip())
        count += 1
        assert test_case > 0
    except EOFError:
        break

assert count > 0

sys.exit(42)



