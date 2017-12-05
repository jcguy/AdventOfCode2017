#!/usr/bin/env python3
# Advent of Code, Problem 2
# James Corder Guy


def main():
    # Part 1
    the_input = []
    with open("problem2.txt") as f:
        for line in f:
            the_input.append(
                    list(
                        map(int, 
                            line.replace("\n", "").split("\t"))))

    checksum = 0

    for line in the_input:
        checksum += max(line) - min(line)

    print("Part 1: {}".format(checksum))

    # Part 2
    checksum = 0
    row_done = False

    for line in the_input:
        sorted_line = sorted(line, reverse=True)
        for i, n in enumerate(sorted_line):
            for _, m in enumerate(sorted_line, start=(i + 1)):
                if (n % m) == 0 and n != m:
                    print(n, m)
                    checksum += n // m
                    row_done = True
                    break

            if row_done:
                row_done = False
                break

    print("Part 2: {}".format(checksum))




if __name__ == "__main__":
    main()
