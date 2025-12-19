input = open("input.txt")
lines = input.readlines()

def overclock_joltage(bank: str) -> int:
    def inner(start_idx: int, remaining: int) -> int:
        largest = 0
        largest_idx = 0
        # print(f"{start_idx}, {len(bank) - remaining + 1}")
        print("")
        for i in range(start_idx, len(bank) - remaining + 1):
            print(i)
            v = int(bank[i])
            if v > largest:
                # print(v)
                largest = v
                largest_idx = i
        if remaining > 1:

            return largest * 10**(remaining -1) + inner(largest_idx + 1, remaining - 1)
        else:
            return largest
    return inner(0, 12)


print(overclock_joltage("987654321111111"))


# total = 0
# for l in lines:
#     total += overclock_joltage(l.strip())
# print(total)