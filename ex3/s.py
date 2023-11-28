from collections import Counter

def main():
    N, V = map(int, input().split())
    parents: list[None|int] = [None]*V
    for _ in range(N):
        a,b = map(int, input().split())
        parents[b]=a
    leaves = set(range(V)) - set(parents)
    count = Counter()
    for i in leaves:
        root = i
        while parents[root] is not None:
            root = parents[root]
        count[root]+=1
    print(count.most_common(1)[0][0]) 

main()

