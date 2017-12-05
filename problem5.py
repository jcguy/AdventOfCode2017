#!/usr/bin/env python3
# Advent of Code, Problem 5
# James Corder Guy


def main():
    # Part 1
    instructions = []
    with open("problem5.txt") as f:
        for line in f:
            instructions.append(int(line.replace("\n", "")))

    i = 0
    steps = 0
    while i < len(instructions):
        instructions[i] += 1
        i += instructions[i] - 1
        steps += 1

    print("Part 1: {}".format(steps))

    # Part 2
    instructions = []
    with open("problem5.txt") as f:
        for line in f:
            instructions.append(int(line.replace("\n", "")))

    i = 0
    steps = 0
    while i < len(instructions):
        steps += 1

        if instructions[i] < 3:
            instructions[i] += 1
            i += instructions[i] - 1
        else:
            instructions[i] -= 1
            i += instructions[i] + 1

    print("Part 2: {}".format(steps))




if __name__ == "__main__":
    main()
