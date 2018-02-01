#!/usr/bin/env python3
# Advent of Code, Problem 8
# James Corder Guy


def main():
    # Part 1
    instructions = []
    with open("problem8.txt") as f:
        for line in f:
            instructions.append(line.replace("\n", "").split())

    registers = {}
    maximum = -1

    for i in instructions:
        register = i[0]
        instruction = i[1]
        change = i[2]
        condition = i[4]
        comparison = i[5]
        value = i[6]

        if register not in registers.keys():
            registers[register] = 0

        if condition not in registers.keys():
            registers[condition] = 0

        if eval("registers[\"" + condition + "\"]" + comparison + value):
            if instruction == "inc":
                registers[register] += int(change)
                if registers[register] > maximum:
                    maximum = registers[register]
            else:
                registers[register] -= int(change)
                if registers[register] > maximum:
                    maximum = registers[register]

    print("Part 1: {}".format(max(registers.values())))
    print("Part 2: {}".format(maximum))




if __name__ == "__main__":
    main()
