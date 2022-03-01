def puissance(a, n):
    if n == 0:
        return 1
    else:
        return a * puissance(a, n-1)


def puissance_mod(a,n):
    if n == 0:
        return 1

    if n%2==0:
        return puissance_mod(a*a, n//2)
    else:
        return a*puissance_mod(a*a, (n-1)//2)

import matplotlib.pyplot as plt
import time

def t(k):
    t0 = time.time()
    puissance(3,k)
    t1 =  time.time() - t0

    t0 = time.time()
    puissance_mod(3,k)
    t2 = time.time() - t0
    return (t1, t2)

n = list(range(200))
times = [t(k) for k in n]
plt.plot(n, times)
plt.show()