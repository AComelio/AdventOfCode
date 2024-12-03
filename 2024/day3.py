import sys
sys.path.append('..')

from utils import *
import re

input_func = lambda x: tuple(map(int, x.split(' ')))

example_input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

test_pairs_part1 = [
    (example_input, 161),
]

example_input_2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

test_pairs_part2 = [
    (example_input_2, 48),
]


@time_me
def part1(input_str):
    match_str = r'mul\(\d{1,3}\,\d{1,3}\)'
    matches = re.findall(match_str, input_str)
    return sum((eval(m.replace('mul', '').replace(',', '*')) for m in matches))

@time_me
def part2(input_str):
    match_str = r"(mul\(\d{1,3}\,\d{1,3}\))|(don't\(\))|(do\(\))"
    matches = (''.join(m) for m in re.findall(match_str, input_str))
    state = True
    total = 0
    for match in matches:
        if 'mul(' in match:
            total += state * eval(match.replace('mul', '').replace(',', '*'))
        else:
            state = not "don't" in match
    return total

if __name__ == '__main__':
    run_tests(part1, test_pairs_part1)
    print()
    input_str = request_problem_input(day=3, year=2024)
    print(f'Part 1 answer: {part1(input_str)}')
    print()
    run_tests(part2, test_pairs_part2)
    print()
    print(f'Part 2 answer: {part2(input_str)}')

