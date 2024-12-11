import numpy as np
from itertools import combinations


def get_unique_freqs(data_):
    unique_letters = np.unique(data_)
    unique_freqs = np.delete(unique_letters, np.argwhere(unique_letters == '.'))
    return unique_freqs


def in_grid(data_, coords) -> bool:
    if 0 <= coords[0] < data_.shape[0] and 0 <= coords[1] < data_.shape[1]:
        return True
    return False


def solve_part1(data_: np.array):
    unique_freqs = get_unique_freqs(data_)

    antinodes = []
    for freq in unique_freqs:
        freq_coords = np.array(np.where(data_ == freq)).T
        if freq_coords.shape[0] < 2:
            continue
        for pair in combinations(freq_coords, 2):
            direction = pair[1] - pair[0]
            candidates = [pair[1] + direction, pair[0] - direction]
            for candidate in candidates:
                if in_grid(data_, candidate):
                    antinodes.append(candidate)
    antinodes = np.unique(antinodes, axis=0)
    return antinodes.shape[0]


def solve_part2(data_: np.array):
    unique_freqs = get_unique_freqs(data_)

    antinodes = []
    for freq in unique_freqs:
        freq_coords = np.array(np.where(data_ == freq)).T
        if freq_coords.shape[0] < 2:
            continue
        for pair in combinations(freq_coords, 2):
            direction = pair[1] - pair[0]
            i = 0
            while in_grid(data_, pair[1] + direction * i):
                antinodes.append(pair[1] + direction * i)
                i += 1
            i = 0
            while in_grid(data_, pair[0] - direction * i):
                antinodes.append(pair[0] - direction * i)
                i += 1
    antinodes = np.unique(antinodes, axis=0)
    return antinodes.shape[0]


if __name__ == '__main__':
    with open('input.txt') as f:
        data = np.array([list(line) for line in f.read().splitlines()])

    print(solve_part1(data))
    print(solve_part2(data))
