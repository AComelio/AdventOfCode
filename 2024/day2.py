import sys
sys.path.append('..')

from utils import *

input_func = lambda x: tuple(map(int, x.split(' ')))

example_input = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''
example_input = tuple(map(input_func, example_input.split('\n')))

test_pairs_part1 = [
    (example_input, 2),
]

test_pairs_part2 = [
    (example_input, 4),
]

def check_report(report):
    previous_value = report[0]
    if report[0] < report[1]:
        state = lambda x, y: x < y
    elif report[0] > report[1]:
        state = lambda x, y: x > y
    else:
        return False
    for value in report[1:]:
        if not state(previous_value, value):
            return False
        if abs(previous_value - value) > 3:
            return False
        previous_value = value
    else:
        return True

@time_me
def part1(vals):
    safe_reports = 0
    for report in vals:
        safe_reports += check_report(report)
    return safe_reports

@time_me
def part2(vals):
    safe_reports = 0
    for report in vals:
        permutations = list()
        permutations.append(report)
        for i in range(len(report)):
            permutations.append(report[:i] + report[i+1:])
        safe_reports += any(check_report(permutation)
                            for permutation in permutations)
    return safe_reports

if __name__ == '__main__':
    run_tests(part1, test_pairs_part1)
    print()
    vals = request_problem_input(day=2, year=2024)
    vals = tokenise_input_file(vals, func=input_func)
    print(f'Part 1 answer: {part1(vals)}')
    print()
    run_tests(part2, test_pairs_part2)
    print()
    print(f'Part 2 answer: {part2(vals)}')

