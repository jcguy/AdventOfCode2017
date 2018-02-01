#!/usr/bin/env python3
# Advent of Code, Problem 9
# James Corder Guy


def main():
    # Part 1
    data = []
    with open("problem9.txt") as f:
        for line in f:
            data.append(line.replace("\n", ""))
    data = data[0]

    processed = ""
    skip_next = False
    in_garbage = False
    char_count = 0

    for c in data:
        if skip_next:
            skip_next = False

        elif c == "!":
            skip_next = True

        elif c == "<" and not in_garbage:
            in_garbage = True

        elif c == ">":
            in_garbage = False

        elif in_garbage:
            char_count += 1

        elif not in_garbage:
            processed += c


    current_value = 0
    total_score = 0

    for c in processed:
        if c == "{":
            current_value += 1

        elif c == "}":
            total_score += current_value
            current_value -= 1

    print("Part 1: " + str(total_score))
    print("Part 2: " + str(char_count))




if __name__ == "__main__":
    main()
