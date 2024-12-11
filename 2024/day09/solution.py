def decompress_data(data_) -> list:
    extended_data = []
    id_ = 0
    for i in range(len(data_)):
        if i % 2:
            extended_data.extend([None] * data_[i])
        else:
            extended_data.extend([id_] * data_[i])
            id_ += 1
    return extended_data


def calculate_checksum(data) -> int:
    checksum = 0
    for i, val in enumerate(data):
        if val is None:
            continue
        checksum += val * i
    return checksum


def solve_part1(data_: list) -> int:
    extended_data = decompress_data(data_)

    no_data_index = extended_data.index(None)
    for i in reversed(range(len(extended_data))):
        if no_data_index == i:
            break
        if extended_data[i] is None:
            continue
        else:
            extended_data[no_data_index] = extended_data[i]
            extended_data[i] = None
            no_data_index = extended_data.index(None)
    return calculate_checksum(extended_data)


def divide_in_blocks(flat_data: list) -> list[dict]:
    block_borders = [0]
    for i in range(1, len(flat_data)):
        if flat_data[i] != flat_data[i - 1]:
            block_borders.append(i)
    block_borders.append(len(flat_data))

    blocked_data = []
    for i in range(1, len(block_borders)):
        ind_start = block_borders[i - 1]
        ind_end = block_borders[i]
        data_block = flat_data[ind_start:ind_end]
        blocked_data.append({'id': data_block[0],'start': ind_start, 'length': len(data_block), 'data': data_block})
    blocked_data = [block for block in blocked_data if block['id'] is not None]
    return blocked_data


def move_data_block(data: list, source_start: int, source_length: int, target_start: int) -> list:
    for i in range(0, source_length):
        data[target_start + i] = data[source_start + i]
        data[source_start + i] = None
    return data


def solve_part2(data_: list) -> int:
    extended_data = decompress_data(data_)
    blocked_data = divide_in_blocks(extended_data)

    for block in reversed(blocked_data):
        free_start = None
        for i, val in enumerate(extended_data):
            if val is None:
                if free_start is None:
                    free_start = i
            else:
                free_start = None
                continue
            if i >= block['start']:
                break
            if (i - free_start) + 1 == block['length']:
                extended_data = move_data_block(extended_data, block['start'], block['length'], free_start)
                break
    return calculate_checksum(extended_data)


if __name__ == '__main__':
    with open('input.txt') as f:
        raw_data = f.read()
    # raw_data = '2333133121414131402'
    data = list(map(int, raw_data.strip()))
    print(solve_part1(data))
    print(solve_part2(data))
