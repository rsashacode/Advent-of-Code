import pytest
from solution import solve_part1, solve_part2

INPUT_PART1 = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
INPUT_PART2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

def test_part1():
    assert solve_part1(INPUT_PART1) == 161

def test_part2():
    assert solve_part2(INPUT_PART2) == 48


if __name__ == "__main__":
    retcode = pytest.main(["-x", r"2024\day03\test.py"])
