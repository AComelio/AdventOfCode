import sys
sys.path.append('../AdventOfCode')

from utils import *

test_pairs_part1 = [
    ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 7),
    ('bvwbjplbgvbhsrlpgdmjqwftvncz', 5),
    ('nppdvjthqldpwncqszvftbrmjlhg', 6),
    ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10),
    ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11),
]

test_pairs_part2 = [
    ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 19),
    ('bvwbjplbgvbhsrlpgdmjqwftvncz', 23),
    ('nppdvjthqldpwncqszvftbrmjlhg', 23),
    ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 29),
    ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 26),
]

@time_me
def part1(vals):
    for i in range(4, len(vals)):
        s = vals[i-4:i]
        if len(set(s)) == 4:
            return i

@time_me
def part2(vals):
    for i in range(14, len(vals)):
        s = vals[i-14:i]
        if len(set(s)) == 14:
            return i

if __name__ == '__main__':
    run_tests(part1, test_pairs_part1)
    print()
    with open('2022/day6.txt', 'r') as f:
        vals = f.read()
    print(f'Part 1 answer: {part1(vals)}')
    print()
    run_tests(part2, test_pairs_part2)
    print()
    print(f'Part 2 answer: {part2(vals)}')