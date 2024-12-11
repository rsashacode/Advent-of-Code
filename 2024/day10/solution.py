import numpy as np
from collections import deque


def find_trailheads(data_: np.array) -> list[tuple]:
    trailheads_coords = np.array(np.where(data_ == 0)).T
    return [tuple(trailhead) for trailhead in trailheads_coords]


def score_rate_trailhead(map_: np.array, trailhead: tuple, rating_mode: bool) -> np.array:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    points = 0

    visited = set(trailhead)
    queue = deque()
    queue.append(trailhead)

    while queue:
        x, y = queue.popleft()
        if map_[x][y] == 9:
            points += 1
            continue

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if (
                    0 <= new_x < map_.shape[0] and
                    0 <= new_y < map_.shape[1] and
                    (
                        rating_mode or
                        (new_x, new_y) not in visited
                    )
            ):
                if map_[new_x][new_y] - map_[x][y] == 1:
                    queue.append((new_x, new_y))
                    visited.add((new_x, new_y))
    return points


def solve_part1(map_: np.array) -> np.array:
    trailheads = find_trailheads(data)
    return sum(score_rate_trailhead(map_, trailhead, rating_mode=False) for trailhead in trailheads)


def solve_part2(map_: np.array) -> np.array:
    trailheads = find_trailheads(data)
    return sum(score_rate_trailhead(map_, trailhead, rating_mode=True) for trailhead in trailheads)


if __name__ == '__main__':
    with open('input.txt') as f:
        data_raw = f.read()
    data = np.array([list(map(int, line.strip())) for line in data_raw.splitlines()])

    print(solve_part1(data))
    print(solve_part2(data))