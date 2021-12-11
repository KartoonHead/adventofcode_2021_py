import os
import sys


INPUT_TXT = "../Input/07_TheTreacheryOfWhales.txt"


def get_input():
    with open(os.path.join(sys.path[0], INPUT_TXT), "r") as my_input:
        return my_input.read()


def parse_input(txt: str) -> list:
    return list(map(int, txt.split(",")))


def get_fuel_consumption_for_position(position, crabs):
    fuel_consumption = 0
    for crab in crabs:
        fuel_consumption += abs(crab - position)
    return fuel_consumption


def get_fuel_consumption_for_position_part2(position, crabs):
    fuel_consumption = 0
    for crab in crabs:
        steps = abs(crab - position)
        fuel_consumption += int((steps**2 + steps)/2)
    return fuel_consumption


def magic():
    txt = get_input()
    crabs = parse_input(txt)
    fuel_consumption_by_index = list()
    for i in range(0, max(crabs)+1):
        fuel_consumption_by_index.append(get_fuel_consumption_for_position(i, crabs))
    min_fuel = min(fuel_consumption_by_index)
    position = fuel_consumption_by_index.index(min_fuel)
    print(">>> Minimum fuel consumption found at {} with consumption of {} fuel".format(position, min_fuel))

    fuel_consumption_by_index = list()
    for i in range(0, max(crabs)+1):
        fuel_consumption_by_index.append(get_fuel_consumption_for_position_part2(i, crabs))
    min_fuel = min(fuel_consumption_by_index)
    position = fuel_consumption_by_index.index(min_fuel)
    print(">>> Minimum fuel consumption (with adjusted consumption model) found at {} with consumption of {} fuel".format(position, min_fuel))


magic()
