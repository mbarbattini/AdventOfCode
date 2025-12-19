import os

cwd = os.getcwd()


def part1():
    # file = open(f'{cwd}/input.txt')
    file = open(f'{cwd}/test.txt')
    ranges = file.readline().split(',')
    total = 0
    for ele in ranges:
        first, last = ele.split('-')
        max_digits = len(last) // 2
        curr = 1
        while len(str(curr)) <= max_digits:
            test = str(curr) + str(curr) # duplicate chars
            if int(test) <= int(last) and int(test) >= int(first):
                total += int(test)
            curr += 1

    return total


def part2():
    file = open(f'{cwd}/input.txt')
    # file = open(f'{cwd}/test.txt')
    ranges = file.readline().split(',')
    total = 0
    for ele in ranges:
        first, last = ele.split('-')
        max_digits = len(last) // 2
        curr = 1
        count_this = False
        accepted = []
        while len(str(curr)) <= max_digits:
            n_dupl = len(last) // len(str(curr))
            i = 1
            test = str(curr)
            while i < n_dupl:
                test += str(curr) # duplicate chars
                if int(test) > int(last):
                    break
                i += 1
                if int(test) <= int(last) and int(test) >= int(first) and test not in accepted:
                    accepted.append(test)
                    total += int(test)
                    print(test)
            curr += 1

    return total



if __name__ == '__main__':
    total = part1()
    print(f"part 1: {total}")
    total = part2()
    print(f"part 2: {total}")
