import pytest
from solution import make_array, solve_part1, solve_part2

INPUT = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

def test_part1():
    assert solve_part1(make_array(INPUT)) == 18

def test_part2():
    assert solve_part2(make_array(INPUT)) == 9


if __name__ == "__main__":
    retcode = pytest.main(["-x", r"2024\day04\test.py"])
