from functools import cache


@cache
def execute_rules(stone: int, n_blinks: int) -> int:
    if n_blinks == 0:
        return 1
    elif stone == 0:
        stone = 1
        return execute_rules(stone, n_blinks - 1)
    elif len(str(stone)) % 2 == 0:
        str_stone = str(stone)
        len_stone = len(str_stone)
        middle_index = len_stone // 2
        left_stone = int(str_stone[:middle_index])
        right_stone = int(str_stone[middle_index:])
        return execute_rules(left_stone, n_blinks - 1) + execute_rules(right_stone, n_blinks - 1,)
    else:
        return execute_rules(stone * 2024, n_blinks - 1)


def solve(stones: list, n_blinks=25) -> int:
    n_stones = 0
    for stone in stones:
        print(f"Stone: {stone}")
        n_stones += execute_rules(stone, n_blinks)
    return n_stones


if __name__ == '__main__':
    with open('input.txt') as f:
        data_raw = f.read()
    data = list(map(int, data_raw.split()))
    print(solve(data, n_blinks=75))
