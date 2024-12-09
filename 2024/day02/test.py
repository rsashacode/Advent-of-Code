import pytest
from solution import solve_part1, solve_part2

INPUT = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

def test_part1():
    assert solve_part1(INPUT) == 2

def test_part2():
    assert solve_part2(INPUT) == 4


if __name__ == "__main__":
    retcode = pytest.main(["-x", r"2024\day02\test.py"])
