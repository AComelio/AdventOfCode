import sys
sys.path.append('..')

from utils import *
from collections import defaultdict
import networkx as nx

def input_func(i):
    i = i.split('\n\n')
    r = defaultdict(set)
    for rule in i[0].split('\n'):
        p = tuple(map(int, rule.split('|')))
        r[p[0]].add(p[1])
    u = tuple(map(lambda x: tuple(map(int, x.split(','))),
                  i[1].split('\n')))
    return r, u

example_input = '''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''
example_input = input_func(example_input)

test_pairs_part1 = [
    (example_input, 143),
]

test_pairs_part2 = [
    (example_input, 123),
]


@time_me
def part1(inputs):
    rules, updates = inputs
    total = 0
    for update in updates:
        seen_pages = set()
        for page in update:
            if seen_pages & rules[page]:
                break
            seen_pages.add(page)
        else:
            total += update[len(update)//2]
    return total

@time_me
def part2(inputs):
    rules, updates = inputs
    bad_updates = list()
    for update in updates:
        seen_pages = set()
        for page in update:
            if seen_pages & rules[page]:
                bad_updates.append(update)
                break
            seen_pages.add(page)
    total = 0
    for update in bad_updates:
        update_pages = set(update)
        graph = nx.DiGraph()
        for page in update:
            if page in rules:
                graph.add_edges_from((page, p2) for p2 in rules[page]
                                                 if p2 in update_pages)
        hierarchy = {n: i for i, n in enumerate(nx.topological_sort(graph))}
        fixed_update = tuple(sorted(update,
                                    key=lambda x: hierarchy[x]
                                   )
                            )
        total += fixed_update[len(fixed_update)//2]
    return total

if __name__ == '__main__':
    run_tests(part1, test_pairs_part1)
    print()
    inputs = input_func(request_problem_input(day=5, year=2024))
    print(f'Part 1 answer: {part1(inputs)}')
    print()
    run_tests(part2, test_pairs_part2)
    print()
    print(f'Part 2 answer: {part2(inputs)}')



