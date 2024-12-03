import sys
sys.path.append('..')

from utils import *
from collections import Counter

input_func = lambda x: list(map(int, x.split('   ')))

example_input = '''3   4
4   3
2   5
1   3
3   9
3   3'''
example_input = list(map(input_func, example_input.split('\n')))

test_pairs_part1 = [
    (example_input, 11),
]

test_pairs_part2 = [
    (example_input, 31),
]

@time_me
def part1(vals):
    l1, l2 = list(), list()
    for r, l in vals:
        l1.append(r)
        l2.append(l)
    return sum(map(lambda x: abs(x[0] - x[1]), zip(sorted(l1), sorted(l2))))

@time_me
def part2(vals):
    l1, l2 = list(), list()
    for r, l in vals:
        l1.append(r)
        l2.append(l)
    counts = Counter(l2)
    return sum(v * counts[v] for v in l1)

if __name__ == '__main__':
    run_tests(part1, test_pairs_part1)
    print()
    vals = request_problem_input(day=1, year=2024)
    vals = tokenise_input_file(vals, func=input_func)
    print(f'Part 1 answer: {part1(vals)}')
    print()
    run_tests(part2, test_pairs_part2)
    print()
    print(f'Part 2 answer: {part2(vals)}')
