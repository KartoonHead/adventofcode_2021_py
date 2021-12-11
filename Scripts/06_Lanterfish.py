import os
import sys


INPUT_TXT = "../Input/06_Lanternfish.txt"


def get_input():
    with open(os.path.join(sys.path[0], INPUT_TXT), "r") as my_input:
        return my_input.read()


def parse_input(txt: str):
    return list(map(int, txt.split(",")))


def age_and_spawn_fish(num_of_fish_by_age):
    new_fish_to_spawn = num_of_fish_by_age[0]
    for i in range(8):
        num_of_fish_by_age[i] = num_of_fish_by_age[i+1]
    num_of_fish_by_age[6] += new_fish_to_spawn
    num_of_fish_by_age[8] = new_fish_to_spawn


def magic(days):
    txt = get_input()
    fishes = parse_input(txt)
    num_of_fish_by_age = list()
    for i in range(9):
        num_of_fish_by_age.append(fishes.count(i))
    for i in range(days):
        age_and_spawn_fish(num_of_fish_by_age)
    result = sum(num_of_fish_by_age)
    print(">> Total number of lanternfish after {} days is {}".format(days, result))


magic(80)
magic(256)
