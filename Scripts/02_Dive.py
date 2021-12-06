import os
import sys


INPUT_TXT = "../Input/02_Dive.txt"

DIR_FWD = "forward"
DIR_DWN = "down"
DIR_UP = "up"


class Boat1:
    def __init__(self):
        self.position = [0, 0]

    def forward(self, amount):
        self.position[1] += amount

    def up(self, amount):
        self.position[0] -= amount

    def down(self, amount):
        self.position[0] += amount


class Boat2:
    def __init__(self):
        self.position = [0, 0]
        self.aim = 0

    def forward(self, amount):
        self.position[0] += amount
        self.position[1] += amount * self.aim

    def up(self, amount):
        self.aim -= amount

    def down(self, amount):
        self.aim += amount


def get_input():
    with open(os.path.join(sys.path[0], INPUT_TXT), "r") as my_input:
        return my_input.read()


def parse_input(txt: str) -> list:
    return txt.splitlines()


def magic(my_boat):
    txt = get_input()
    commands = parse_input(txt)

    for command in commands:
        direction, space, amount = command.partition(' ')
        amount = int(amount)

        if direction == DIR_FWD:
            my_boat.forward(amount)
        elif direction == DIR_UP:
            my_boat.up(amount)
        elif direction == DIR_DWN:
            my_boat.down(amount)

    print(my_boat.position[0] * my_boat.position[1])


magic(Boat1())
magic(Boat2())
