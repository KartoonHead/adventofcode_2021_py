import os
import sys


INPUT_TXT = "../Input/03_BinaryDiagnostic.txt"


def get_input():
    with open(os.path.join(sys.path[0], INPUT_TXT), "r") as my_input:
        return my_input.read()


def parse_input(txt: str) -> list:
    return [int(num, 2) for num in txt.splitlines()]


def most_common_bit(numbers, i):
    ones, zeroes = 0, 0
    for num in numbers:
        shift_num = num >> i
        if shift_num & 0b01:
            ones += 1
        else:
            zeroes += 1
    if ones >= zeroes:
        return 1
    return 0


def get_gamma_epsilon_rates(numbers, length):
    gamma_rate = 0
    epsilon_rate = 0
    for i in range(length):
        if most_common_bit(numbers, i):
            gamma_rate += 1 << i
        else:
            epsilon_rate += 1 << i
    return gamma_rate, epsilon_rate


def get_oxygen_co2_rates(numbers, length):
    o2_numbers = numbers.copy()
    co2_numbers = numbers.copy()
    for i in range(length):
        i_inv = length - 1 - i
        if len(o2_numbers) > 1:
            o2_winning_bit = most_common_bit(o2_numbers, i_inv)
            o2_numbers = [num for num in o2_numbers if int((num >> i_inv) & 0x01) == o2_winning_bit]
        if len(co2_numbers) > 1:
            co2_winning_bit = most_common_bit(co2_numbers, i_inv)
            co2_numbers = [num for num in co2_numbers if int((num >> i_inv) & 0x01) != co2_winning_bit]
    return o2_numbers[0], co2_numbers[0]


def magic():
    txt = get_input()
    length = len(txt.splitlines()[0])
    numbers = parse_input(txt)
    gamma_rate, epsilon_rate = get_gamma_epsilon_rates(numbers, length)
    o2, co2 = get_oxygen_co2_rates(numbers, length)
    print("Power consumption = " + str(gamma_rate * epsilon_rate))
    print("Life support rating = " + str(o2 * co2))


magic()
