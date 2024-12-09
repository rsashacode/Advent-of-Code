import pytest
from solution import solve_part1, solve_part2


INPUT = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

field = [[char for char in line] for line in INPUT.splitlines() if line != ""]
field = tuple(field)

def test_part1():
    assert solve_part1(field) == 41


def test_part2():
    assert solve_part2(field) == 6

if __name__ == "__main__":
    retcode = pytest.main(["-x", r"2024\day06\test.py"])
