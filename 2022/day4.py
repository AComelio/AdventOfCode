import sys
sys.path.append('../AdventOfCode')

from utils import *

input_func = lambda x: tuple(map(lambda y: tuple(map(int, y.split('-'))), x.split(',')))

example_input = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''
example_input = list(map(input_func, example_input.split('\n')))

test_pairs_part1 = [
    (example_input, 2),
]

test_pairs_part2 = [
    (example_input, 4),
]

@time_me
def part1(vals):
    def is_subrange_of(r1, r2):
        return r1[0] >= r2[0] and r1[1] <= r2[1]
    return sum(is_subrange_of(p1, p2) or is_subrange_of(p2, p1) for p1, p2 in vals)

@time_me
def part2(vals):
    def overlaps(r1, r2):
        return (r2[0] <= r1[0] <= r2[1]
             or r2[0] <= r1[1] <= r2[1]
             or r1[0] <= r2[0] <= r1[1]
             or r1[0] <= r2[1] <= r1[1])
    return sum(overlaps(p1, p2) for p1, p2 in vals)

if __name__ == '__main__':
    run_tests(part1, test_pairs_part1)
    print()
    vals = tokenise_input_file('2022/day4.txt', func=input_func)
    print(f'Part 1 answer: {part1(vals)}')
    print()
    run_tests(part2, test_pairs_part2)
    print()
    print(f'Part 2 answer: {part2(vals)}')
