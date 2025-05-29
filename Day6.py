n = 100
nsum = 0.0
def ak(k):
    return 4* (-1)**(k-1) / (2*k -1)
for k in range(1, n+1):
    nsum = nsum + ak(k)

print("sum(from 1 to n) =", nsum)
