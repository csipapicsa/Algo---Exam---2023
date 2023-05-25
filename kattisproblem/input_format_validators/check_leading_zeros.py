#! /usr/env/python3

import sys

def assert_no_leading_zero(string_int):
    assert len(string_int) > 0
    assert string_int[0] != '0' or len(string_int) == 1



n_string = input().strip()
assert_no_leading_zero(n_string)
n = int(n_string)

for _ in range(n):
    info = input().strip().split(':')

    name = info[0].strip()
    assert_no_leading_zero(name)
    time = info[1].strip()
    assert_no_leading_zero(name)
    dependencies_str = info[3].strip()

    if dependencies_str:
        for string in dependencies_str.strip().split(' '):
            assert_no_leading_zero(string)
            int_ = int(string)
            assert 0 <= int_ < n


while True:
    try:
        t = input().strip()
        assert_no_leading_zero(t)

    except EOFError:
        break

sys.exit(42)