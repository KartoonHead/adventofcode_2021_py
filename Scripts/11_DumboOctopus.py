import os
import sys


INPUT_TXT = "../Input/11_DumboOctopus.txt"


class Octopuses:
    def __init__(self, energy_levels, width, height):
        self._energy_levels = energy_levels
        self.width = width
        self.height = height
        self._flashes = list()

    def step(self):
        self._flashes = list()
        for x in range(self.width):
            for y in range(self.height):
                self._increment_coords(x, y)
        for flashed in self._flashes:
            self._energy_levels[flashed[0]][flashed[1]] = 0
        return self._flashes

    def _increment_coords(self, x, y):
        self._energy_levels[x][y] += 1
        if self._energy_levels[x][y] > 9:
            self._flash(x, y)

    def _flash(self, x, y):
        coords = [x, y]
        if coords not in self._flashes:
            self._flashes.append(coords)
        else:
            return
        for ix in [-1, 0, 1]:
            for iy in [-1, 0, 1]:
                if ix == 0 and iy == 0:
                    continue
                else:
                    neighbour_x = x + ix
                    neighbour_y = y + iy
                    if self._are_valid_coords(neighbour_x, neighbour_y):
                        self._increment_coords(neighbour_x, neighbour_y)

    def _are_valid_coords(self, x, y):
        if x < 0 or y < 0:
            return False
        elif x >= self.width or y >= self.height:
            return False
        else:
            return True


def get_input() -> str:
    with open(os.path.join(sys.path[0], INPUT_TXT), "r") as my_input:
        return my_input.read()


def parse_input(txt: str) -> list:
    as_ints = list()
    for line in txt.splitlines():
        as_ints.append([int(char) for char in line])
    return as_ints


def magic():
    txt = get_input()
    energy_levels = parse_input(txt)
    width = len(energy_levels)
    height = len(energy_levels[0])
    Octos = Octopuses(energy_levels, width, height)
    num_octos = width * height
    total_flashes = 0
    step = 0
    while True:
        flashes_this_step = len(Octos.step())
        total_flashes += flashes_this_step
        if step == 99:
            print(">>> Part One: number of flashes after 100 steps is {}".format(total_flashes))
        if flashes_this_step == num_octos:
            print(">>> Part Two: all octos flash for the first time on step {}".format(step + 1))
            break
        step += 1


magic()
