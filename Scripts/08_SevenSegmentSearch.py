import os
import sys


INPUT_TXT = "../Input/08_SevenSegmentSearch.txt"
ABCDEFG = "abcdefg"
NUM_SEGS = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
UNIQUE_LENGTHS = [2, 3, 4, 7]


class Display:
    def __init__(self, display):
        self.solution = ""
        self.wiring = display[0].split()
        self.output = display[1].split()
        self.wavefunction = dict()
        for letter in ABCDEFG:
            self.wavefunction[letter] = ABCDEFG
        self._constrain_by_unique_length()
        self._solve_output()

    def _constrain_by_unique_length(self):
        for wired_number in self.wiring:
            segment_length = len(wired_number)
            if segment_length in UNIQUE_LENGTHS:
                template_output = [NUM for NUM in NUM_SEGS if len(NUM) == segment_length][0]
                template_intersection = ""
                for l in ABCDEFG:
                    if l not in template_output:
                        template_intersection += l
                for letter in ABCDEFG:
                    if letter not in wired_number:
                        for template_segment in template_output:
                            self.wavefunction[letter] = self.wavefunction[letter].replace(template_segment, "")
                    else:
                        for template_segment in template_intersection:
                            self.wavefunction[letter] = self.wavefunction[letter].replace(template_segment, "")

    def _solve_output(self):
        for num in self.output:
            # Easy solutions for unique length numbers
            if len(num) in UNIQUE_LENGTHS:
                for i in range(len(NUM_SEGS)):
                    if len(NUM_SEGS[i]) == len(num):
                        self.solution += str(i)
            else:
                potential_configurations = list()
                for char in num:
                    possible_connections = self.wavefunction[char]
                    if len(potential_configurations) == 0:
                        for connection in possible_connections:
                            potential_configurations.append(connection)
                    else:
                        new_configurations = list()
                        for connection in possible_connections:
                            for potential_configuration in potential_configurations:
                                if connection not in potential_configuration:
                                    new_configuration = potential_configuration + connection
                                    new_configurations.append(new_configuration)
                        potential_configurations = new_configurations

                potential_configurations = ["".join(sorted(config)) for config in potential_configurations]
                potential_configurations = list(set(potential_configurations))
                for potential_configuration in potential_configurations:
                    for i, segs in enumerate(NUM_SEGS):
                        if potential_configuration == segs:
                            self.solution += str(i)
                            break


def get_input():
    with open(os.path.join(sys.path[0], INPUT_TXT), "r") as my_input:
        return my_input.read()


def parse_input(txt: str) -> list:
    return [line.split(" | ") for line in txt.splitlines()]


def magic():
    txt = get_input()
    parsed_input = parse_input(txt)
    print(parsed_input)

    ones_fours_sevens_eights = ""
    total = 0
    for line in parsed_input:
        display = Display(line)
        ones_fours_sevens_eights += display.solution
        total += int(display.solution)

    ones = ones_fours_sevens_eights.count("1")
    fours = ones_fours_sevens_eights.count("4")
    sevens = ones_fours_sevens_eights.count("7")
    eights = ones_fours_sevens_eights.count("8")
    print(">>> Part One: 1, 4, 7, and 8 appear {} times.".format(ones + fours + sevens + eights))
    print(">>> Part Two: the total of all output values is {}.".format(total))


magic()
