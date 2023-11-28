

EMPTY = 0
STOP = 1
WALL = 2

VALUES: dict[str, int] = {".": EMPTY, "o": STOP, "#": WALL, "P": EMPTY, "X": EMPTY}

def solve(ether: list[list[int]], init_pos: tuple[int, int], goal_pos: tuple[int, int]):
    done = {init_pos}
    stack = [init_pos]
    new_stack: list[tuple[int, int]] = []
    distance = 0
    while stack and goal_pos not in done:
        distance += 1
        for i, j in stack:
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ni, nj = i, j
                while ether[ni + di][nj + dj] != WALL:
                    ni += di
                    nj += dj
                    if ether[ni][nj] == STOP:
                        break
                if (ni, nj) not in done:
                    done.add((ni, nj))
                    new_stack.append((ni, nj))
        stack, new_stack = new_stack, []
    print(distance if goal_pos in done else -1)


def main():
    H, _ = map(int, input().split())
    ether: list[list[int]] = []
    init_pos = 0, 0
    goal_pos = 0, 0
    for i in range(H):
        row: list[int] = []
        for j, c in enumerate(input()):
            row.append(VALUES[c])
            if c == "P":
                init_pos = i, j
            elif c == "X":
                goal_pos = i, j
        ether.append(row)
    solve(ether, init_pos, goal_pos)


main()

