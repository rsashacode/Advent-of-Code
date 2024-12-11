import numpy as np
from numba import jit
from math import floor, log10


def execute_rule_1(stone: int) -> list:
    return [1]


def execute_rule_2(stone: int, len_stone: int) -> list:
    left = stone // 10**(len_stone//2)
    right = stone % 10**(len_stone//2)
    return [left, right]


def execute_rule_3(stone: int) -> list:
    return [stone * 2024]


def execute_rules(stones: list[int]) -> list:
    result = []
    for stone in stones:
        if stone == 0:
            result.extend(execute_rule_1(stone))
        else:
            len_stone = floor(log10(stone)) + 1
            if len(str(stone)) % 2 == 0:
                result.extend(execute_rule_2(stone, len_stone))
            else:
                result.extend(execute_rule_3(stone))
    return result


def solve(data_: list, n_blinks=25) -> int:
    i = 1
    for _ in range(n_blinks):
        print(f"Blink: {i}")
        data_ = execute_rules(data_)
        i += 1
    return len(data_)


if __name__ == '__main__':
    with open('input.txt') as f:
        data_raw = f.read()
    data = list(map(int, data_raw.split()))
    print(solve(data, n_blinks=25))
