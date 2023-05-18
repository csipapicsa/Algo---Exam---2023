MOD = 10**9 + 9
M = []

# https://open.kattis.com/problems/cardmagic?tab=metadata

def solve(n, t):
    if n <= 0 or t <= 0:
        return 0
    if n == 1:
        return int(t <= K)
    if M[n][t] >= 0:
        return M[n][t]
    res = 0
    for k in range(1, min(K, t) + 1):
        res = (res + solve(n - 1, t - k)) % MOD
    M[n][t] = res
    return res

n, K, t = map(int, input().split())
M = [[-1] * (t + 1) for _ in range(n + 1)]
print(solve(n, t))