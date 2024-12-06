import sys
sys.path.append('..')

from utils import *
from copy import deepcopy

def input_func(input_str):
    starting_chars = {'v', '>', '<', '^'}
    grid = dict()
    for y, row in enumerate(input_str.split('\n')):
        for x, cell in enumerate(row):
            grid[(x, y)] = cell
            if cell in starting_chars:
                start_loc = (x, y)
    return grid, start_loc

example_input = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''
example_input = input_func(example_input)

test_pairs_part1 = [
    (example_input, 41),
]

test_pairs_part2 = [
    (example_input, 6),
]


@time_me
def part1(vals):
    grid, loc = vals
    cycle = ('^', '>', 'v', '<')
    move_funcs = {
        '^': lambda x: (x[0],   x[1]-1),
        '>': lambda x: (x[0]+1, x[1]),
        '<': lambda x: (x[0]-1, x[1]),
        'v': lambda x: (x[0],   x[1]+1),
    }
    state = grid[loc]
    state_ind = cycle.index(state)
    visited_locs = set()
    visited_locs.add(loc)
    while True:
        check_loc = move_funcs[state](loc)
        if check_loc not in grid:
            break
        if grid[check_loc] == '#':
            state_ind = (state_ind + 1) % 4
            state = cycle[state_ind]
        loc = move_funcs[state](loc)
        visited_locs.add(loc)
    return len(visited_locs)

@time_me
def part2(vals):
    starting_grid, starting_loc = vals
    grid = deepcopy(starting_grid)
    loc = starting_loc
    cycle = ('^', '>', 'v', '<')
    move_funcs = {
        '^': lambda x: (x[0],   x[1]-1),
        '>': lambda x: (x[0]+1, x[1]),
        '<': lambda x: (x[0]-1, x[1]),
        'v': lambda x: (x[0],   x[1]+1),
    }
    starting_state = grid[loc]
    state = starting_state
    starting_state_ind = cycle.index(state)
    state_ind = starting_state_ind
    visited_locs = set()
    visited_locs.add((loc, state))
    while True:
        check_loc = move_funcs[state](loc)
        if check_loc not in grid:
            break
        if grid[check_loc] == '#':
            state_ind = (state_ind + 1) % 4
            state = cycle[state_ind]
        loc = move_funcs[state](loc)
        visited_locs.add((loc, state))
    valid_spots = 0
    first_pass_visited = deepcopy(visited_locs)
    for potential_obstruction, _ in first_pass_visited - {(starting_loc, starting_state),}:
        grid = deepcopy(starting_grid)
        grid[potential_obstruction] = '#'
        visited_locs = deepcopy(first_pass_visited)
        loc = starting_loc
        state = starting_state
        state_ind = starting_state_ind
        reached_change = False
        while True:
            check_loc = move_funcs[state](loc)
            if not reached_change:
                reached_change = check_loc == potential_obstruction
            if check_loc not in grid:
                break
            if grid[check_loc] == '#':
                state_ind = (state_ind + 1) % 4
                state = cycle[state_ind]
            loc = move_funcs[state](loc)
            if reached_change and ((loc, state) in visited_locs):
                valid_spots += 1
                break
    return valid_spots

if __name__ == '__main__':
    run_tests(part1, test_pairs_part1)
    print()
    vals = input_func(request_problem_input(day=6, year=2024))
    print(f'Part 1 answer: {part1(vals)}')
    print()
    run_tests(part2, test_pairs_part2)
    print()
    print(f'Part 2 answer: {part2(vals)}')

