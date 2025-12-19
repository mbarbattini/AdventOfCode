import numpy as np
import time

def part1(nRows, nCols, path):
    f = open(path)
    arr = np.zeros((nRows, nCols), dtype=np.str_)

    j = 0

    for line in f.readlines():
        for i in range(len(line.strip())):
            arr[j,i] = line[i]
        j += 1

    def inBounds(j,i):
        return j >= 0 and j <= nRows-1 and i >= 0 and i <= nCols-1

    total = 0
    for j in range(nRows):
        for i in range(nCols):
            # print(f"{i},{j}")
            current = arr[j,i]
            if current != "@": continue

            n_neighbors = 0

            if inBounds(j,i+1):
                if arr[j,i+1] == "@":
                    n_neighbors += 1
            if inBounds(j,i-1):
                if arr[j,i-1] == "@":
                    n_neighbors += 1

            if inBounds(j-1,i):
                if arr[j-1,i] == "@":
                    n_neighbors += 1

            if inBounds(j+1,i):
                if arr[j+1,i] == "@":
                    n_neighbors += 1

            if inBounds(j+1,i+1):
                if arr[j+1,i+1] == "@":
                    n_neighbors += 1

            if inBounds(j+1,i-1):
                if arr[j+1,i-1] == "@":
                    n_neighbors += 1

            if inBounds(j-1,i+1):
                if arr[j-1,i+1] == "@":
                    n_neighbors += 1

            if inBounds(j-1,i-1):
                if arr[j-1,i-1] == "@":
                    n_neighbors += 1

            if n_neighbors < 4:
                total += 1

    return total


def part2(nRows, nCols, path):
    f = open(path)
    arr = np.zeros((nRows, nCols), dtype=np.str_)

    j = 0

    for line in f.readlines():
        for i in range(len(line.strip())):
            arr[j,i] = line[i]
        j += 1

    def inBounds(j,i):
        return j >= 0 and j <= nRows-1 and i >= 0 and i <= nCols-1
    
    total = 0
    newState = np.zeros((nRows, nCols), dtype=np.str_)
    
    while True:

        this_total = 0
        for j in range(nRows):
            for i in range(nCols):
                current = arr[j,i]
                if current != "@": continue

                n_neighbors = 0

                if inBounds(j,i+1):
                    if arr[j,i+1] == "@":
                        n_neighbors += 1
                if inBounds(j,i-1):
                    if arr[j,i-1] == "@":
                        n_neighbors += 1

                if inBounds(j-1,i):
                    if arr[j-1,i] == "@":
                        n_neighbors += 1

                if inBounds(j+1,i):
                    if arr[j+1,i] == "@":
                        n_neighbors += 1

                if inBounds(j+1,i+1):
                    if arr[j+1,i+1] == "@":
                        n_neighbors += 1

                if inBounds(j+1,i-1):
                    if arr[j+1,i-1] == "@":
                        n_neighbors += 1

                if inBounds(j-1,i+1):
                    if arr[j-1,i+1] == "@":
                        n_neighbors += 1

                if inBounds(j-1,i-1):
                    if arr[j-1,i-1] == "@":
                        n_neighbors += 1

                if n_neighbors < 4:
                    this_total += 1
                    # remove this roll
                    newState[j,i] = '.'
                else:
                    # keep it the same
                    newState[j,i] = arr[j,i]

        arr = newState

        if this_total == 0:
            return total
        else:
            total += this_total


def main():
    startTime = time.time()
    p1 = part1(138,138, "input.txt")
    print(f"Part 1: {p1} in {time.time() - startTime:.3f} s")
    startTime = time.time()
    p2 = part2(138,138, "input.txt")
    print(f"Part 2: {p2} in {time.time() - startTime:.3f} s")

main()