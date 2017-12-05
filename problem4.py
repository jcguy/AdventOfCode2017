#!/usr/bin/env python3
# Advent of Code, Problem 4
# James Corder Guy


def main():
    # Part 1
    num_valid = 0
    with open("problem4.txt") as f:
        for line in f:
            phrase = line.replace("\n", "").split(" ")
            if sorted(phrase) == sorted(list(set(phrase))):
                num_valid += 1

    print("Part 1: {}".format(num_valid))

    # Part 2
    num_valid = 0
    with open("problem4.txt") as f:
        for line in f:
            phrase = line.replace("\n", "").split(" ")
            new_phrase = []

            for word in phrase:
                new_phrase.append("".join(sorted(word)))

            phrase = new_phrase

            if sorted(phrase) == sorted(list(set(phrase))):
                num_valid += 1

    print("Part 2: {}".format(num_valid))




if __name__ == "__main__":
    main()
