#!/usr/bin/env python3
# Advent of Code, Problem 10
# James Corder Guy


def main():
    the_list = list(range(256))
    current_position = 0
    skip_size = 0
    lengths = [46, 41, 212, 83, 1, 255, 157, 65, 139, 52, 39, 254, 2, 86, 0, 204]

    for length in lengths:
        for i in range((length // 2) + 1):
            temp = the_list[(current_position + i) % len(the_list)]
            the_list[(current_position + i) % len(the_list)] = the_list[(current_position + length - i) % len(the_list)]
            the_list[(current_position + length - i) % len(the_list)] = temp

        current_position += length + skip_size
        current_position = current_position % len(the_list)
        skip_size += 1

    print("Part 1: " + str(the_list[0] * the_list[1]))




if __name__ == "__main__":
    main()
