import sys
sys.path.append('../AdventOfCode')

from utils import *

input_func = lambda x: list(map(int, x.split('\n')))

example_input = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''
example_input = list(map(input_func, example_input.split('\n\n')))

test_pairs_part1 = [
    (example_input, 24000),
]

test_pairs_part2 = [
    (example_input, 45000),
]

@time_me
def part1(elf_bags):
    totals = map(sum, elf_bags)
    return max(totals)

@time_me
def part2(elf_bags):
    totals = map(sum, elf_bags)
    return sum(sorted(totals, reverse=True)[:3])

if __name__ == '__main__':
    run_tests(part1, test_pairs_part1)
    print()
    vals = tokenise_input_file('2022/day1.txt', seperator='\n\n', func=input_func)
    print(f'Part 1 answer: {part1(vals)}')
    print()
    run_tests(part2, test_pairs_part2)
    print()
    print(f'Part 2 answer: {part2(vals)}')
