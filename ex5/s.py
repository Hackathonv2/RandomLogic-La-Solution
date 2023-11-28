

def solve(nbase, team_list):
    tot = nbase + sum(team_list)
    tot_needed = tot // 2 + 1
    additional_needed = tot_needed - nbase
    if additional_needed <= 0:
        return 0
    dp = [False for _ in range(tot-nbase+1)]
    dp[0] = True
    for team in team_list:
        for i in range(tot-nbase, team-1, -1):
            dp[i] |= dp[i-team]
    for i in range(additional_needed, len(dp)):
        if dp[i]:
            return i

nbase = int(input())
ls = []
for i in range(int(input())):
    ls.append(int(input()))

print(solve(nbase, ls))
