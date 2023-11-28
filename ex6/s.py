

from itertools import product

i = 0
length = int(input())
ALL = set("".join(t) for t in product("RVB", repeat=5))
for i in range(length):
    s = input()
    T = [(col, int(k)) for col, k in s.split()]
    REM = {c for c in ALL if all(c[k - 1] != col for col, k in T)}
    ALL.difference_update(REM)
    if not ALL:
        break
solprint(str(i))


