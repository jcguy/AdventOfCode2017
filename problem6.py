#!/usr/bin/env python3
# Advent of Code, Problem 5
# James Corder Guy


def main():
    # Part 1
    the_input = [4, 10, 4, 1, 8, 4, 9, 14, 5, 1, 14, 15, 0, 15, 3, 5]

    state = the_input[:]
    previous_configs = []

    while True:
        previous_configs.append(state[:])
        biggest = state.index(max(state))
        carrying = state[biggest]
        state[biggest] = 0

        i = biggest + 1
        while carrying > 0:
            state[i % len(state)] += 1
            carrying -= 1
            i += 1

        if state in previous_configs:
            print("Part 1: {}".format(len(previous_configs)))
            previous_configs.append(state[:])
            break

    # Part 2
    first_occurence = previous_configs.index(previous_configs[-1])
    print("Part 2: {}".format(len(previous_configs) - 1 - first_occurence))


if __name__ == "__main__":
    main()
