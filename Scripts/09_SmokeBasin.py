import os
import sys


INPUT_TXT = "../Input/09_SmokeBasin.txt"


class HeightMap:
    def __init__(self, lines):
        self.grid = lines
        self.width = len(lines)
        self.height = len(lines[0])

    def get_height(self, x, y):
        return self.grid[x][y]

    def get_neighbours(self, x, y):
        neighbours = list()
        for ix in [-1, 0, 1]:
            for iy in [-1, 0, 1]:
                if ix == 0 and iy == 0:
                    continue
                elif abs(ix) == abs(iy):
                    continue
                else:
                    x_to_sample = x + ix
                    y_to_sample = y + iy
                    if self.are_valid_coords(x_to_sample, y_to_sample):
                        neighbours.append([x_to_sample, y_to_sample])
        return neighbours

    def get_neighbour_heights(self, x, y):
        neighbour_cells = self.get_neighbours(x, y)
        return [self.get_height(n[0], n[1]) for n in neighbour_cells]

    def are_valid_coords(self, x, y):
        if x < 0 or y < 0:
            return False
        elif x >= self.width or y >= self.height:
            return False
        else:
            return True

    def find_low_points(self):
        low_points = list()
        for x in range(self.width):
            for y in range(self.height):
                is_low_point = True
                height_here = self.get_height(x, y)
                neighbour_heights = self.get_neighbour_heights(x, y)
                for neighbour_height in neighbour_heights:
                    if neighbour_height <= height_here:
                        is_low_point = False
                        break
                if is_low_point:
                    low_points.append([x, y])
        return low_points

    def expand_to_basin(self, x, y):
        basin = [[x, y]]
        new_perimeter = [[x, y]]
        while len(new_perimeter) > 0:
            sample_point = new_perimeter.pop()
            neighbours = self.get_neighbours(sample_point[0], sample_point[1])
            cells_to_add = [n for n in neighbours if self.get_height(n[0], n[1]) < 9]
            cells_to_add = [n for n in cells_to_add if n not in basin]
            new_perimeter.extend(cells_to_add)
            basin.extend(cells_to_add)
        return basin

    def find_basins(self):
        low_points = self.find_low_points()
        return [self.expand_to_basin(lp[0], lp[1]) for lp in low_points]


def get_input():
    with open(os.path.join(sys.path[0], INPUT_TXT), "r") as my_input:
        return my_input.read()


def parse_input(txt: str) -> list:
    grid = list()
    lines = txt.splitlines()
    for line in lines:
        grid.append([int(c) for c in line])
    return grid


def magic():
    txt = get_input()
    parsed_input = parse_input(txt)
    heightmap = HeightMap(parsed_input)
    low_points = heightmap.find_low_points()
    total = 0
    for xy in low_points:
        total += heightmap.get_height(xy[0], xy[1]) + 1
    print(">>> Part One: sum of the risk levels of all low points is {}".format(total))
    basins = heightmap.find_basins()
    basin_sizes = list()
    for basin in basins:
        basin_sizes.append(len(basin))
    basin_sizes.sort()
    big_three = basin_sizes[-3:]
    result = big_three[0] * big_three[1] * big_three[2]
    print(">>> Part Two: three largest basins multiplied together: {}".format(result))


magic()
