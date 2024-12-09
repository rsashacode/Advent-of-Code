import numpy as np

from scipy.signal import convolve2d, convolve


def make_array(data_: str) -> np.array:
    return np.array([list(line) for line in data_.splitlines() if line != ""])


def get_n_targets(arr_: np.ndarray, target_:str) -> int:
    slices = []
    _n_targets = 0

    # Horizontal slices
    for i in range(len(arr_)):
        slices.append(arr_[i, :])

    # Diagonal slices
    n_diags_one_way = len(arr_) - (len(target_) - 1)
    for i in range(-1 * n_diags_one_way, n_diags_one_way + 1):
        slices.append(np.diag(arr_, k=i))

    for sl in slices:
        sl_str = ''.join(list(sl))
        _n_targets += sl_str.count(target_)
    return _n_targets


def solve_part1(data_arr_: np.ndarray, target_: str='XMAS') -> int:
    n_targets = 0
    for k in range(4):
        n_targets += get_n_targets(arr_=np.rot90(data_arr_, k=k), target_=target_)
    return n_targets


def solve_part2(data_arr_: np.ndarray) -> int:
    mapper = np.vectorize(ord)
    data_arr_mapped = mapper(data_arr_)

    x_mas_kernel = np.array(
        [
            [1 / ord('M'), 0, 1 / ord('S')],
            [0, 1 / ord('A'), 0],
            [1 / ord('M'), 0, 1 / ord('S')]
        ]
    )

    result = 0
    for k in range(4):
        kernel_rotated = np.rot90(x_mas_kernel, k)
        convolutions = convolve2d(data_arr_mapped, kernel_rotated, mode='valid')
        result += np.count_nonzero(convolutions == 5)
    return result


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()
    data_arr = make_array(data)
    print(solve_part1(data_arr))
    print(solve_part2(data_arr))
