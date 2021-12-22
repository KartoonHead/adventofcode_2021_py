import os
import sys


INPUT_TXT = "../Input/10_SyntaxScoring.txt"
CHAR_SCORE_LUT = {")": 3, "]": 57, "}": 1197, ">": 25137}
CHAR_COMP_SCORE_LUT = {"(": 1, "[": 2, "{": 3, "<": 4}
OPEN_CHARS = "([{<"
CLOSE_TO_OPEN = {")": "(", "]": "[", "}": "{", ">": "<"}
OPEN_TO_CLOSE = {"(": ")", "[": "]", "{": "}", "<": ">"}


def get_input():
    with open(os.path.join(sys.path[0], INPUT_TXT), "r") as my_input:
        return my_input.read()


def magic():
    illegal_chars = list()
    completion_scores = list()
    program = get_input()
    for i, line in enumerate(program.splitlines()):
        corrupted = False
        stack = ""
        for char in line:
            if char in OPEN_CHARS:
                stack += char
            else:
                if stack[-1] == CLOSE_TO_OPEN[char]:
                    stack = stack[:-1]
                else:
                    expected_char = OPEN_TO_CLOSE[stack[-1]]
                    print("Illegal character detected on line {} - Expected {}, found {}".format(i, expected_char, char))
                    illegal_chars.append(char)
                    corrupted = True
                    break

        if not corrupted:
            comp_score = 0
            for char in reversed(stack):
                comp_score *= 5
                comp_score += CHAR_COMP_SCORE_LUT[char]
            completion_scores.append(comp_score)

    corruption_score = 0
    for char in illegal_chars:
        corruption_score += CHAR_SCORE_LUT[char]
    print(">>> Part One: corruption score is {}".format(corruption_score))

    completion_scores.sort()
    mid = int((len(completion_scores) - 1) * 0.5)
    print(">>> Part Two: middle auto correct score is {}".format(completion_scores[mid]))


magic()
