def diff_(x: list) -> list:
    return [x[i+1] - x[i] for i in range(len(x)-1)]


def is_safe(arr_: list) -> bool:
    ds = diff_(arr_)
    if all([i > 0 for i in ds]) or all(i < 0 for i in ds):
        if all([abs(i) <= 3 for i in ds]):
            return True
    return False


def solve(data_: str, use_problem_dampener: bool) -> int:
    counter = 0
    for ln in data_.splitlines():
        arr_ = [int(i) for i in ln.split()]
        if is_safe(arr_):
            counter += 1
        else:
            if use_problem_dampener:
                for i in range(len(ln)):
                    arr_n = [arr_[j] for j in range(len(arr_)) if j != i]
                    if is_safe(arr_n):
                        counter += 1
                        break
    return counter


def solve_part1(_data: str) -> int:
    return solve(_data, False)


def solve_part2(_data: str) -> int:
    return solve(_data, True)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()
    print(solve_part1(data))
    print(solve_part2(data))