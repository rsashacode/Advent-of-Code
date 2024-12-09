import re


def solve_part1(data_: str) -> int:
    matches = re.findall(
        r"mul\((\d{1,3}),(\d+)\)",
        data_
    )
    return sum([int(pair[0]) * int(pair[1]) for pair in matches])


def solve_part2(data_: str) -> int:
    matches = re.findall(
        r"mul\((\d{1,3}),(\d+)\)|(do\(\))|(don't\(\))",
        data_
    )

    matches = [[it for it in row if it != ""] for row in matches]

    s = 0
    do = True
    for match in matches:
        if do:
            if len(match) == 2:
                s += int(match[0]) * int(match[1])
        if len(match) == 1:
            if match[0] == "don't()":
                do = False
            elif match[0] == "do()":
                do = True
    return s


if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read()
    print(solve_part1(data))
    print(solve_part2(data))