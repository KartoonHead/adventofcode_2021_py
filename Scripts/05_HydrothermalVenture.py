import os
import sys


INPUT_TXT = "../Input/05_HydrothermalVenture.txt"


class OceanFloor:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0] * width for _i in range(height)]

    def mark_line(self, line):
        x1, y1 = line[0]
        x2, y2 = line[1]
        x_steps = x1 - x2
        y_steps = y1 - y2
        x_dir, y_dir = 0, 0
        if x_steps > 0:
            x_dir = -1
        elif x_steps < 0:
            x_dir = 1
        if y_steps > 0:
            y_dir = -1
        elif y_steps < 0:
            y_dir = 1

        num_steps = max(abs(x_steps), abs(y_steps))

        mark_x, mark_y = line[0]
        for i in range(num_steps):
            self.mark_coords(mark_x, mark_y)
            mark_x += x_dir
            mark_y += y_dir
        self.mark_coords(mark_x, mark_y)

    def mark_coords(self, x, y):
        self.grid[x][y] += 1

    def get_number_of_double_overlaps(self):
        number_of_doubles = 0
        for x in range(self.width):
            for y in range(self.height):
                if self.grid[x][y] >= 2:
                    number_of_doubles += 1
        return number_of_doubles


def get_input():
    with open(os.path.join(sys.path[0], INPUT_TXT), "r") as my_input:
        return my_input.read()


def parse_input(txt: str):
    string_lines = [line.split(" -> ") for line in txt.splitlines()]
    parsed_input = list()
    for line in string_lines:
        string_coords_a = line[0]
        string_coords_b = line[1]
        string_coords_a = list(map(int, string_coords_a.split(",")))
        string_coords_b = list(map(int, string_coords_b.split(",")))
        parsed_input.append([string_coords_a, string_coords_b])
    return parsed_input


def is_diagonal(line):
    if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
        return False
    return True


def magic():
    txt = get_input()
    lines = parse_input(txt)
    of = OceanFloor(1000, 1000)
    for line in lines:
        if not is_diagonal(line):
            of.mark_line(line)
    print("Part one: {}".format(of.get_number_of_double_overlaps()))
    for line in lines:
        if is_diagonal(line):
            of.mark_line(line)
    print("Part two: {}".format(of.get_number_of_double_overlaps()))


magic()
