from itertools import product
from operator import mul, add
from typing import Callable


def concat(num1: int, num2: int) -> int:
    return int(str(num1) + str(num2))


def solve(data_: list[list], operators: list[Callable]):
    answer = 0
    for eq in data_:
        total = eq[0]
        inputs = eq[1:]
        total = int(total)
        n_positions = len(inputs) - 1
        cases = product(operators, repeat=n_positions)
        for case in cases:
            res = case[0](inputs[0], inputs[1])
            for i in range(1, n_positions):
                res = case[i](res, inputs[i+1])
            if res == total:
                answer += total
                break
    return answer


def solve_part1(data_: list[list]):
    return solve(data_, [mul, add])


def solve_part2(data_: list[list]):
    return solve(data_, [mul, add, concat])


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        data_str = f.read()
    data = [list(map(int, line.replace(":", "").split())) for line in data_str.strip().splitlines()]
    print(solve_part1(data))
    print(solve_part2(data))
