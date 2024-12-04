import sys
sys.path.append('..')

from utils import *
import re

example_input = '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''

test_pairs_part1 = [
    (example_input, 18),
]

test_pairs_part2 = [
    (example_input, 9),
]


@time_me
def part1(input_str):
    input_lines = input_str.split('\n')
    width = len(input_lines[0])
    depth = len(input_lines)
    diagonals = width + depth -1
    match_str = 'XMAS'
    revered_input = ''.join(reversed(input_str))
    vertical_input = [[] for _ in range(width)]
    for i, row in enumerate(input_lines):
        for j, letter in enumerate(row):
            vertical_input[j].append(letter)
    vertical_input = '\n'.join(map(lambda x: ''.join(x), vertical_input))
    reversed_vertical_input = ''.join(reversed(vertical_input))
    upwards_diagonal = [[] for _ in range(diagonals)]
    for j in range(depth):
        x = 0
        y = j
        while (0 <= x < width) and (0 <= y < depth):
            upwards_diagonal[j].append(input_lines[y][x])
            y -= 1
            x += 1
    for i in range(1, width):
        x = i
        y = j
        while (0 <= x < width) and (0 <= y < depth):
            upwards_diagonal[j+i].append(input_lines[y][x])
            y -= 1
            x += 1
    upwards_diagonal = '\n'.join(map(lambda x: ''.join(x), upwards_diagonal))
    reversed_upwards_diagonal = ''.join(reversed(upwards_diagonal))
    downwards_diagonal = [[] for _ in range(diagonals)]
    for j in range(depth):
        x = 0
        y = depth - j - 1
        while (0 <= x < width) and (0 <= y < depth):
            downwards_diagonal[j].append(input_lines[y][x])
            y += 1
            x += 1
    for i in range(1, width):
        x = i
        y = 0
        while (0 <= x < width) and (0 <= y < depth):
            downwards_diagonal[j+i].append(input_lines[y][x])
            y += 1
            x += 1
    downwards_diagonal = '\n'.join(map(lambda x: ''.join(x), downwards_diagonal))
    reversed_downwards_diagonal = ''.join(reversed(downwards_diagonal))

    return sum(map(len, [re.findall(match_str, input_str),
                         re.findall(match_str, revered_input),
                         re.findall(match_str, vertical_input),
                         re.findall(match_str, reversed_vertical_input),
                         re.findall(match_str, upwards_diagonal),
                         re.findall(match_str, reversed_upwards_diagonal),
                         re.findall(match_str, downwards_diagonal),
                         re.findall(match_str, reversed_downwards_diagonal)
                        ]
                  )
               )

@time_me
def part2(input_str):
    input_grid = tuple(map(tuple, input_str.split('\n')))
    width = len(input_grid[0])
    depth = len(input_grid)
    chars = {'M', 'S'}
    count = 0
    for y in range(1, depth-1):
        for x in range(1, width-1):
            if input_grid[y][x] != 'A':
                continue
            tl = input_grid[y-1][x-1]
            tr = input_grid[y-1][x+1]
            bl = input_grid[y+1][x-1]
            br = input_grid[y+1][x+1]
            if {tl, tr, bl, br} != chars:
                continue
            count += tl != br and tr != bl
    return count

if __name__ == '__main__':
    run_tests(part1, test_pairs_part1)
    print()
    input_str = request_problem_input(day=4, year=2024)
    print(f'Part 1 answer: {part1(input_str)}')
    print()
    run_tests(part2, test_pairs_part2)
    print()
    print(f'Part 2 answer: {part2(input_str)}')

