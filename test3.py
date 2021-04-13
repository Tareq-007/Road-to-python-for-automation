n=int(input())
for r in range(n,-1,-1):
    for c in range(r, 0, -1):
        print("*",end="")
    print()