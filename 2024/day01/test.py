import pytest
from solution import make_df, solve_part1, solve_part2

INPUT = """
3   4
4   3
2   5
1   3
3   9
3   3
"""

def test_part1():
    data_df = make_df(INPUT)
    assert solve_part1(data_df) == 11

def test_part2():
    data_df = make_df(INPUT)
    assert solve_part2(data_df) == 31


if __name__ == "__main__":
    retcode = pytest.main(["-x", r"2024\day01\test.py"])
