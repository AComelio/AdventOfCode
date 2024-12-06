import sys
sys.path.append('..')

from utils import *

input_func = lambda x: x

example_input = ''

test_pairs_part1 = [
    (example_input, None),
]

example_input_2 = ''

test_pairs_part2 = [
    (example_input_2, None),
]


@time_me
def part1(input_str):
    pass

@time_me
def part2(input_str):
    pass

if __name__ == '__main__':
    run_tests(part1, test_pairs_part1)
    print()
    input_str = request_problem_input(day=6, year=2024)
    vals = tokenise_input_file(input_str, input_func)
    print(f'Part 1 answer: {part1(vals)}')
    print()
    run_tests(part2, test_pairs_part2)
    print()
    print(f'Part 2 answer: {part2(vals)}')
