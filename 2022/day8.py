import sys
sys.path.append('../AdventOfCode')

from utils import *

example_input = '''30373
25512
65332
33549
35390'''
example_input = example_input.split('\n')

example_input = {(x, y): int(h) for y, row in enumerate(example_input) for x, h in enumerate(row)}

test_pairs_part1 = [
    (example_input, 21),
]

test_pairs_part2 = [
    (example_input, 8),
]

@time_me
def part1(vals):
    visibles = set()

    xmax = max(k[0] for k in vals) + 1
    ymax = max(k[1] for k in vals) + 1

    for x in range(xmax):
        cmax = -1
        for y in range(ymax):
            if vals[(x,y)] > cmax:
                visibles.add((x, y))
                cmax = vals[(x, y)]
        cmax = -1
        for y in reversed(range(ymax)):
            if vals[(x,y)] > cmax:
                visibles.add((x, y))
                cmax = vals[(x, y)]
    for y in range(ymax):
        rmax = -1
        for x in range(xmax):
            if vals[(x,y)] > rmax:
                visibles.add((x, y))
                rmax = vals[(x, y)]
        rmax = -1
        for x in reversed(range(xmax)):
            if vals[(x,y)] > rmax:
                visibles.add((x, y))
                rmax = vals[(x, y)]
    return len(visibles)

@time_me
def part2(vals):
    xmax = max(k[0] for k in vals) + 1
    ymax = max(k[1] for k in vals) + 1
    best_score = 0

    for x in range(1, xmax-1):
        for y in range(1, ymax-1):
            h = vals[(x, y)]
            up_dist, right_dist, down_dist, left_dist = 0, 0, 0, 0
            for step in range(1, x+1):
                down_dist += 1
                if vals[(x-step, y)] >= h:
                    break
            for step in range(1, y+1):
                left_dist += 1
                if vals[(x, y-step)] >= h:
                    break

            for step in range(1, xmax-x):
                up_dist += 1
                if vals[(x+step, y)] >= h:
                    break
            for step in range(1, ymax-y):
                right_dist += 1
                if vals[(x, y+step)] >= h:
                    break
            if (up_dist * right_dist * down_dist * left_dist) > best_score:
                best_score = up_dist * right_dist * down_dist * left_dist
    return best_score

if __name__ == '__main__':
    run_tests(part1, test_pairs_part1)
    print()
    vals = tokenise_input_file('2022/day8.txt')
    vals = {(x, y): int(h) for y, row in enumerate(vals) for x, h in enumerate(row)}
    print(f'Part 1 answer: {part1(vals)}')
    print()
    run_tests(part2, test_pairs_part2)
    print()
    print(f'Part 2 answer: {part2(vals)}')
