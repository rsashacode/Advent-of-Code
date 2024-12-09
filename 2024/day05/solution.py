from collections import defaultdict, deque


def build_rule_graph(rules_: list) -> dict[int: list[int]]:
    graph = defaultdict(list)
    for u, v in rules_:
        graph[u].append(v)
    return graph


def sort_update(update_: list[int], graph: defaultdict[int: list]) -> list:
    """
    Topological sort, BFS
    """
    in_degrees = {node: 0 for node in update_}

    for u in update_:
        for v in graph[u]:
            if v in update_:
                in_degrees[v] += 1

    queue = deque([node for node in update_ if in_degrees[node] == 0])

    if len(queue) != 1:
        raise RuntimeError("Ooops, not DAG!")

    correct_order = []

    while queue:
        node = queue.popleft()
        correct_order.append(node)
        for neighbor in graph[node]:
            if neighbor in in_degrees:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)
    return correct_order


def get_middle_page(update_: list):
    middle_index = len(update_) // 2
    return update_[middle_index]


def solve(rules_: list, updates_: list) -> (int, int):
    total_sum_correct = 0
    total_sum_incorrect_ordered = 0
    for update_ in updates_:
        graph_rules_ = build_rule_graph(rules_)
        correct_update_ = sort_update(update_, graph_rules_)
        if correct_update_ == update_:
            total_sum_correct += get_middle_page(update_)
        else:
            total_sum_incorrect_ordered += get_middle_page(correct_update_)
    return total_sum_correct, total_sum_incorrect_ordered

def solve_part1(rules_: list, updates_: list) -> int:
    return solve(rules_, updates_)[0]


def solve_part2(rules_: list, updates_: list) -> int:
    return solve(rules_, updates_)[1]


if __name__ == '__main__':
    with open('rules.txt', 'r') as f:
        rules = [list(map(int, line.split("|"))) for line in f.readlines()]

    with open('updates.txt', 'r') as f:
        updates = [list(map(int, line.split(","))) for line in f.readlines()]
    print(solve(rules, updates))
