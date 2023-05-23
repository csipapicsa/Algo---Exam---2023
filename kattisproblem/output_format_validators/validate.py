import sys

count = 0
while True:
    try:
        out_ = input()
        count += 1
        assert out_ == "Impossible" or 0 <= int(out_) <= 1000
    except EOFError:
        break
assert count > 0

sys.exit(42)