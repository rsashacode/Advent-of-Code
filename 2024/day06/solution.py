import copy
import numpy as np


def get_obstacles_coords(field_: tuple[list[str], ...]) -> list[complex]:
    coords = []
    for i in range(len(field_)):
        for j in range(len(field_[i])):
            if field_[i][j] == '#':
                coords.append(complex(i, j))
    return coords


def get_pointer_coords(field_: tuple[list[str], ...]) -> complex:
    for i in range(len(field_)):
        for j in range(len(field_[i])):
            if field_[i][j] == '^':
                return complex(i, j)


def in_field(field_: tuple[list[str], ...], pos_: complex) -> bool:
    if 0 <= pos_.real < len(field_):
        if 0 <= pos_.imag < len(field_[int(pos_.real)]):
            return True
    return False


def walk(pos_: complex, dir_: complex, obstacles: list[complex]) -> (complex, complex):
    """
    Real number = walk along rows, imag - walk along columns. Change dir = always turn right.
    """
    if pos_ + dir_ in obstacles:
        dir_ *= -1j
    pos_ = pos_ + dir_
    return pos_, dir_


def walk_path(field_: tuple[list[str], ...]) -> tuple[list, bool]:
    obstacles = get_obstacles_coords(field_)
    pos_ = get_pointer_coords(field_)
    dir_ = -1

    visited = set()
    is_in_field = in_field(field_, pos_)
    looped = False
    while is_in_field and not looped:
        visited.add((pos_, dir_))
        pos_, dir_ = walk(pos_, dir_, obstacles)
        is_in_field = in_field(field_, pos_)
        looped = (pos_, dir_) not in visited

    return list({p for p,_ in visited}), (pos_, dir_) in visited


def solve_part1(field_: tuple[list[str], ...]) -> int:
    path = walk_path(field_)[0]
    return len(path)


def solve_part2(field_: tuple[list[str], ...]) -> int:
    walked_path = walk_path(field_)[0]
    n_looped = 0
    counter = 0
    len_path = len(walked_path)
    start_position = get_pointer_coords(field_)
    walked_path = [pos__ for pos__ in walked_path if pos__ != start_position]
    for pos_ in walked_path:
        counter += 1
        print(f"Part2: {counter} / {len_path}")
        new_field_ = copy.deepcopy(field_)
        new_field_[int(pos_.real)][int(pos_.imag)] = '#'
        if walk_path(new_field_)[1]:
            n_looped += 1
    return n_looped


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data_str = f.read()
    field = [[char for char in line] for line in data_str.splitlines() if line != ""]
    field = tuple(field)
    print(solve_part1(field))
    print(solve_part2(field))
