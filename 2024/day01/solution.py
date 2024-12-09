import numpy as np
import pandas as pd


def make_df(_data_str: str) -> pd.DataFrame:
    return pd.DataFrame([line.split() for line in _data_str.strip().split('\n')]).astype(int)


def solve_part1(df: pd.DataFrame) -> int:
    dist = np.abs(df[1].sort_values().values - df[0].sort_values().values).sum()
    return dist


def solve_part2(df: pd.DataFrame) -> int:
    right_col_map = df.groupby(1).count().to_dict()[0]
    similarity_comps = df[0] * df[0].map(right_col_map).fillna(0)
    return int(similarity_comps.sum())


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()
    data_df = make_df(data)
    print("Part1: ", solve_part1(data_df))
    print("Part2: ", solve_part2(data_df))
