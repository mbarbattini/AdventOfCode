def part1():
    f = open("input.txt")
    # f = open("test.txt")
    total = 0
    for l in f.readlines():
        largest = 0
        for i in range(len(l)):
            for j in range(i + 1, len(l)):
                num = l[i] + l[j]
                if int(num) > int(largest):
                    largest = num
        total += int(largest)

    print(f"answer is {total}")


def part2():
    f = open("input.txt")
    # f = open("test.txt")
    total = 0
    for l in f.readlines():
        n_digits = 1
        largest = 0
        i = 0
        j = 1
        while n_digits <= 12:
            if l[i] > l[j]:
                num += l[i]
                j += 1
                i += 1
            else:
                num += l[j]
                i += 2
                j += 1

        total += int(largest)

    print(f"answer is {total}")


def main():
    part1()
    part2()


main()
