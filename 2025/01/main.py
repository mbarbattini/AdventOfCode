import os
cwd = os.getcwd()

# with open(f"{cwd}/1/input.txt") as f:
with open(f"{cwd}/1/test.txt") as f:
    lines = f.readlines()
    sum = 0
    curr = 50
    for l in lines:

        direction = l[0]
        num = l[1:]

        if direction == "L":
            for i in range(int(num)):
                curr -= 1
                if curr % 100 == 0:
                    sum += 1
        if direction == "R":
            for i in range(int(num)):
                curr += 1
                if curr % 100 == 0:
                    sum += 1

    print(f"Answer: {sum}")