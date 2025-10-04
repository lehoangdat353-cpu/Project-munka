a = 125
b = 24

m, n = max(a,b), min(a,b)
while n != 0: # m > n
    r = m % n
    m, n = n, r
print(m)
