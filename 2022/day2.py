import sys
sys.path.append('../AdventOfCode')

from utils import *

input_func = lambda x: tuple(x.split(' '))

example_input = '''A Y
B X
C Z'''
example_input = list(map(input_func, example_input.split('\n')))

test_pairs_part1 = [
    (example_input, 15),
]

test_pairs_part2 = [
    (example_input, 12),
]

@time_me
def part1(vals):
    rules = {
        'A': {'X': 4, 'Y': 8, 'Z': 3},    # Rock
        'B': {'X': 1, 'Y': 5, 'Z': 9},    # Paper
        'C': {'X': 7, 'Y': 2, 'Z': 6},    # Scissors
    }
    scores = {(l, r): rules[l][r] for l in rules for r in rules[l]}
    return sum(scores[row] for row in vals)

@time_me
def part2(vals):
    rules = {
        'A': {'X': 3, 'Y': 4, 'Z': 8},    # Rock
        'B': {'X': 1, 'Y': 5, 'Z': 9},    # Paper
        'C': {'X': 2, 'Y': 6, 'Z': 7},    # Scissors
    }
    scores = {(l, r): rules[l][r] for l in rules for r in rules[l]}
    return sum(scores[row] for row in vals)


if __name__ == '__main__':
    run_tests(part1, test_pairs_part1)
    print()
    vals = tokenise_input_file('2022/day2.txt', func=input_func)
    print(f'Part 1 answer: {part1(vals)}')
    print()
    run_tests(part2, test_pairs_part2)
    print()
    print(f'Part 2 answer: {part2(vals)}')
