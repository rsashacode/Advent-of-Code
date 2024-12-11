import numpy as np
from tqdm.auto import tqdm
from math import floor, log10



def execute_rule_1_vectorized(stones: np.array) -> np.array:
    return np.ones(len(stones), dtype=int)


def execute_rule_2_vectorized(stones: np.array, len_stones: np.array) -> np.array:
    half_len = len_stones // 2
    divisor = 10 ** half_len
    left = list(stones // divisor)
    right = list(stones % divisor)
    return np.concatenate((left, right)).astype(int)


def execute_rule_3_vectorized(stones: np.array) -> np.array:
    return stones * 2024


def execute_rules_vectorized(stones: np.array) -> np.array:
    results = np.empty(0, dtype=int)
    zero_mask = (stones == 0)

    digits_len_stones = np.floor(np.log10(stones, where=~zero_mask)) + 1
    digits_len_stones[zero_mask] = 0
    digits_len_stones = digits_len_stones.astype(np.int32)

    even_mask = (digits_len_stones % 2 == 0)
    else_mask = ~even_mask & ~zero_mask

    if np.any(zero_mask):
        results = np.concatenate([results, execute_rule_1_vectorized(stones[zero_mask])])
    if np.any(even_mask):
        results = np.concatenate([results, execute_rule_2_vectorized(stones[even_mask], digits_len_stones[even_mask])])
    if np.any(else_mask):
        results = np.concatenate([results, execute_rule_3_vectorized(stones[else_mask])])
    return results


def solve_vectorized(data_: list, n_blinks=25):
    data_ = np.array(data_)
    for n_blink in range(n_blinks):
        print(n_blink)
        data_ = execute_rules_vectorized(data_)
    return len(data_)


if __name__ == '__main__':
    with open('input.txt') as f:
        data_raw = f.read()
    data_raw = '125 17 17'
    data = list(map(int, data_raw.split()))
    print(solve_vectorized(data, n_blinks=75))
