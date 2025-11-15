mod = 613123835 + 385120518

MAX = 200010
fact = [1] * MAX
inv_fact = [1] * MAX

def modinv(a):
    return pow(a, mod - 2, mod)

for i in range(1, MAX):
    fact[i] = fact[i-1] * i % mod

inv_fact[MAX-1] = modinv(fact[MAX-1])
for i in range(MAX-2, -1, -1):
    inv_fact[i] = inv_fact[i+1] * (i+1) % mod

def nCr(n, r):
    if r < 0 or r > n:
        return 0
    return fact[n] * inv_fact[r] % mod * inv_fact[n - r] % mod

t = int(input())
out_lines = []
for _ in range(t):
    n = int(input())
    a = input().strip()
    z = a.count('0')
    o = n - z
    if z == 0 or o == 0:
        out_lines.append("0")
        continue
    base = nCr(n - 2, o - 1)
    total = 0
    for j in range(1, n):
        term = base
        if j <= z:
            term = (term - nCr(n - j - 1, o - 1)) % mod
        total = (total + (n - j) * term) % mod
    out_lines.append(str(total))

for res in out_lines:
    print(res)