



D = {"U":(0,1), "D":(0,-1), "R":(1,0), "L":(-1,0)}

ANY = -1

def solve(x:int, dx:int, gx:int):
    if dx == 0:
        return ANY if x==gx else None
    q, r = divmod(gx-x, dx)
    return q if (q>=0 and r==0) else None

def main():
    X,Y = map(int, input().split())
    PATTERN = [D[c] for c in input()]
    L = len(PATTERN)
    DX, DY = (sum(c[i] for c in PATTERN) for i in (0,1))
    res = float("inf")
    posx, posy = 0,0
    for i, (dx, dy) in enumerate(PATTERN):
        resx = solve(posx, DX, X)
        if resx is not None:
            resy = solve(posy, DY, Y)
            if resy is not None:
                if resx == ANY:
                    if resy == ANY:
                        res = min(res, i)
                    else:
                        res = min(res, i + resy*L)
                elif resy == ANY or resy == resx:
                    res = min(res, i+resx*L)
        posx+=dx
        posy+=dy
    if res == float("inf"): print("not possible")
    else: print(res)

main()


