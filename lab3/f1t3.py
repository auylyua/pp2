def solve(numheads, numlegs):
    for chik in range(numheads + 1): 
        rab = numheads - chik 
        if 4 * rab + 2 * chik == numlegs:
            return chik, rab 
    return "No solution"

numheads, numlegs=map(int,input().split())
r = solve(numheads, numlegs)
print(f"chickens, rabbits: {r}")