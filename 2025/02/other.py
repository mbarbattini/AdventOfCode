print(sum(sum([[n for n in range(int(r[0]),int(r[1])+1) if str(n) in (str(n)*2)[1:-1]] for r in [r2.split("-") for r2 in open("input.txt").read().split(",")]],[])))

