import sys
sys.path.append('../AdventOfCode')

from utils import *

from collections import defaultdict, deque

from pprint import pprint

input_func = lambda x: x.split('\n')

example_input = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''
example_input = list(map(input_func, example_input.split('\n\n')))

test_pairs_part1 = [
    (example_input, 'CMZ'),
]

test_pairs_part2 = [
    (example_input, 'MCD'),
]

@time_me
def part1(vals):
    init_state, moves = vals

    stacks = defaultdict(deque)

    for loc, char in enumerate(init_state[-1]):
        if char == ' ':
            continue
        for line in reversed(init_state[:-1]):
            if line[loc] == ' ':
                continue
            stacks[int(char)].append(line[loc])
    for move in moves:
        num, source, dest = map(int, move.replace('move ', '').replace(' from ', ' ').replace(' to ', ' ').split(' '))
        for _ in range(num):
            stacks[dest].append(stacks[source].pop())
    return ''.join(stack.pop() for stack in stacks.values())

@time_me
def part2(vals):
    init_state, moves = vals

    stacks = defaultdict(deque)

    for loc, char in enumerate(init_state[-1]):
        if char == ' ':
            continue
        for line in reversed(init_state[:-1]):
            if line[loc] == ' ':
                continue
            stacks[int(char)].append(line[loc])
    for move in moves:
        num, source, dest = map(int, move.replace('move ', '').replace(' from ', ' ').replace(' to ', ' ').split(' '))
        tmp_stack = deque()
        for _ in range(num):
            tmp_stack.append(stacks[source].pop())
        while tmp_stack:
            stacks[dest].append(tmp_stack.pop())
    return ''.join(stack.pop() for stack in stacks.values())

if __name__ == '__main__':
    run_tests(part1, test_pairs_part1)
    print()
    vals = tokenise_input_file('2022/day5.txt', seperator='\n\n', func=input_func)
    print(f'Part 1 answer: {part1(vals)}')
    print()
    run_tests(part2, test_pairs_part2)
    print()
    print(f'Part 2 answer: {part2(vals)}')
