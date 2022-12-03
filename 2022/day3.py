import sys
sys.path.append('../AdventOfCode')

from utils import *

example_input = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''
example_input = example_input.split('\n')

test_pairs_part1 = [
    (example_input, 157),
]

test_pairs_part2 = [
    (example_input, 70),
]

@time_me
def part1(vals):
    prios = {chr(v+96): v for v in range(1, 27)} | {chr(v+38): v for v in range(27, 53)}
    return sum(prios[tuple(set(row[:len(row)//2]) & set(row[len(row)//2:]))[0]] for row in vals)

@time_me
def part2(vals):
    prios = {chr(v+96): v for v in range(1, 27)} | {chr(v+38): v for v in range(27, 53)}
    return sum(prios[tuple(set(a) & set(b) & set(c))[0]] for a, b, c in zip(*[iter(vals)] * 3))

if __name__ == '__main__':
    run_tests(part1, test_pairs_part1)
    print()
    vals = tokenise_input_file('2022/day3.txt')
    print(f'Part 1 answer: {part1(vals)}')
    print()
    run_tests(part2, test_pairs_part2)
    print()
    print(f'Part 2 answer: {part2(vals)}')
