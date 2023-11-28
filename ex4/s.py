import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

nums = [int(x) for x in lines[0].split(' ')]

snums = sorted(nums, key=lambda x: (nums.count(x), x))
sol = snums[-1] - snums[0]    
print(sol)
