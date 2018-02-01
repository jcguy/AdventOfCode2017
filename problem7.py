#!/usr/bin/env python3
# Advent of Code, Problem 7
# James Corder Guy


class Node:
    def __init__(self):
        self.name = ""
        self.weight = -1
        self.children = []

    def __str__(self):
        ret = self.name + " (" + str(self.weight) + ") "
        if len(self.children) > 0:
            for child in self.children:
                ret += child.name + " "

        return ret

    def total_weight(self):
        if len(self.children) == 0:
            return self.weight
        return self.weight + sum([c.total_weight() for c in self.children])

    def is_balanced(self):
        if len(self.children) == 0:
            return True

        return (len(set([c.total_weight() for c in self.children])) == 1)


def main():
    # Part 1
    data = []
    with open("problem7.txt") as f:
        for line in f:
            data.append(line.replace("\n", "").split())

    nodes = {}
    for line in data:
        nodes[line[0]] = Node()
        nodes[line[0]].name = line[0]
        nodes[line[0]].weight = int(line[1].replace("(", "").replace(")", ""))

    for line in data:
        if "->" in line:
            children = line[line.index("->") + 1:]
            for child in children:
                child = child.replace(",", "")
                nodes[line[0]].children.append(nodes[child])

    print(nodes["utnrb"].weight)
    for node in nodes.values():
        if not node.is_balanced():
            print(node.name + ": ", end='')
            print("[", end='')
            for child in node.children:
                print(child.name + ", " + str(child.total_weight()), end='; ')
            print("]")


if __name__ == "__main__":
    main()
