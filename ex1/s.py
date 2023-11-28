


import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

n = int(lines[0])    
for _ in range(4):
    if n % 3 == 0:
        n //= 3
    elif n % 2 == 0:
        n //= 2
    else:
        n -= 1
print(n)

