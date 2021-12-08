import os
import sys


INPUT_TXT = "../Input/04_GiantSquid.txt"


class Board:
    def __init__(self, rows):
        self.rows = rows
        self.size_x = len(rows[0])
        self.size_y = len(rows)
        self.marks = list()
        for i in range(self.size_y):
            row = list()
            for j in range(self.size_x):
                row.append(False)
            self.marks.append(row.copy())

    def get_number(self, x, y):
        return self.rows[y][x]

    def mark_coords(self, x, y):
        self.marks[y][x] = True

    def get_mark(self, x, y):
        return self.marks[y][x]

    def mark_number(self, num):
        for x in range(self.size_x):
            for y in range(self.size_y):
                if num == self.get_number(x, y):
                    self.mark_coords(x, y)

    def get_unmarked(self):
        unmarked_nums = list()
        for x in range(self.size_x):
            for y in range(self.size_y):
                if not self.get_mark(x, y):
                    unmarked_nums.append(self.get_number(x, y))
        return unmarked_nums

    def has_won(self):
        for y in range(self.size_y):
            row_check = 0
            for x in range(self.size_x):
                if self.get_mark(x, y):
                    row_check += 1
                    if row_check == self.size_y:
                        return True

        for x in range(self.size_x):
            column_check = 0
            for y in range(self.size_y):
                if self.get_mark(x, y):
                    column_check += 1
                    if column_check == self.size_x:
                        return True

        return False


def get_input():
    with open(os.path.join(sys.path[0], INPUT_TXT), "r") as my_input:
        return my_input.read()


def parse_input(txt: str):
    lines = txt.splitlines()
    boards = list()
    board = list()
    callouts = lines[0].split(",")
    callouts = list(map(int, callouts))
    for line in lines[2:]:
        if not line:
            continue
        board.append(list(map(int, line.split())))
        if len(board) == 5:
            boards.append(Board(board.copy()))
            board = list()

    return boards, callouts


def get_winning_board(boards, callouts):
    for number in callouts:
        for board in boards:
            board.mark_number(number)
            if board.has_won():
                return board, number


def get_last_winning_board(boards, callouts):
    for number in callouts:
        for board in boards:
            board.mark_number(number)
        if len(boards) == 1 and boards[0].has_won():
            return boards[0], number
        boards = [board for board in boards if not board.has_won()]


def magic_part1():
    txt = get_input()
    boards, callouts = parse_input(txt)
    winning_board, number = get_winning_board(boards, callouts)
    print(sum(winning_board.get_unmarked()) * number)


def magic_part2():
    txt = get_input()
    boards, callouts = parse_input(txt)
    last_winning_board, last_number = get_last_winning_board(boards, callouts)
    print(last_winning_board.marks)
    print(sum(last_winning_board.get_unmarked()) * last_number)


magic_part1()
magic_part2()
