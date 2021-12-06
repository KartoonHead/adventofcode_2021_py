import os
import sys


INPUT_TXT = "../Input/01_SonarSweep.txt"


def get_input():
    with open(os.path.join(sys.path[0], INPUT_TXT), "r") as my_input:
        return my_input.read()


def parse_input(txt: str) -> list:
    return [int(num) for num in txt.splitlines()]


def part1():
    txt = get_input()
    depths = parse_input(txt)

    increase_depth_count = 0

    for i in range(len(depths)-1):
        if depths[i] < depths[i+1]:
            increase_depth_count += 1

    print(increase_depth_count)


def part2():
    txt = get_input()
    depths = parse_input(txt)

    increase_depth_count = 0

    for i in range(len(depths) - 3):
        this_window = sum(depths[i:i+3])
        next_window = sum(depths[i+1:i+4])

        if this_window < next_window:
            increase_depth_count += 1

    print(increase_depth_count)


part1()
part2()
