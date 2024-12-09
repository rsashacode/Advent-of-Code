import pytest
from solution import solve_part1, solve_part2


RULES = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13"""

UPDATES = """75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

rules = [list(map(int, line.split("|"))) for line in RULES.splitlines()]
updates = [list(map(int, line.split(","))) for line in UPDATES.splitlines()]


def test_part1():
    assert solve_part1(rules, updates) == 143


def test_part2():
    assert solve_part2(rules, updates) == 123


if __name__ == "__main__":
    retcode = pytest.main(["-x", r"2024\day05\test.py"])
