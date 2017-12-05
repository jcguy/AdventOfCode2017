#!/usr/bin/env python3
# Advent of Code, Problem 3
# James Corder Guy

from math import floor

def main():
    # Part 1
    the_input = 347991
    x = 0
    y = 0
    dx = 1
    dy = 0

    length = 1
    completed = 0

    for i in range(1, the_input):
        x += dx
        y += dy
        completed += 1

        if completed == length:
            completed = 0
            dx, dy = dy, dx
            dx *= -1

            if dy == 0:
                length += 1


    distance = abs(x) + abs(y)
    print("Part 1: {}".format(distance))

    # Part 2
    # print("Part 2: {}".format(checksum))




if __name__ == "__main__":
    main()
