import pytest
from solution import solve_part1, solve_part2

INPUT="""190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""


data = [list(map(int, line.replace(":", "").split())) for line in INPUT.strip().splitlines()]


def test_part1():
    assert solve_part1(data) == 3749


def test_part2():
    assert solve_part2(data) == 11387

if __name__ == "__main__":
    retcode = pytest.main(["-x", r"2024\day07\test.py"])

