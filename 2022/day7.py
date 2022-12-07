import sys
sys.path.append('../AdventOfCode')

from utils import *

from collections import deque

example_input = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''
example_input = example_input.split('\n')

test_pairs_part1 = [
    (example_input, 95437),
]

test_pairs_part2 = [
    (example_input, 24933642),
]

class Directory:
    def __init__(self, name, parent):
        self.parent = parent
        self.name = name
        self.sub_dirs = dict()
        self.files = list()
        self.size = 0

    def add_file(self, file):
        self.files.append(file)
        self.update_size(file.size)

    def update_size(self, val):
        self.size += val
        if self.parent is not None:
            self.parent.update_size(val)

    def add_sub_dir(self, name):
        self.sub_dirs[name] = Directory(name, self)

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

@time_me
def part1(vals):
    loc = Directory('/', None)
    home = loc
    vals = iter(vals)
    next(vals)
    for row in vals:
        tokens = row.split()
        if tokens[0] == '$':
            if tokens[1] == 'cd':
                if tokens[2] == '..':
                    loc = loc.parent
                else:
                    loc = loc.sub_dirs[tokens[2]]
        elif tokens[0] == 'dir':
            if tokens[1] not in loc.sub_dirs:
                loc.add_sub_dir(tokens[1])
        else:
            f = File(tokens[1], int(tokens[0]))
            loc.add_file(f)
    total = 0
    q = deque()
    q.append(home)
    while q:
        l = q.pop()
        if l.size <= 100000:
            total += l.size
        q.extend(l.sub_dirs.values())
    return total

@time_me
def part2(vals):
    loc = Directory('/', None)
    home = loc
    vals = iter(vals)
    next(vals)
    for row in vals:
        tokens = row.split()
        if tokens[0] == '$':
            if tokens[1] == 'cd':
                if tokens[2] == '..':
                    loc = loc.parent
                else:
                    loc = loc.sub_dirs[tokens[2]]
        elif tokens[0] == 'dir':
            if tokens[1] not in loc.sub_dirs:
                loc.add_sub_dir(tokens[1])
        else:
            f = File(tokens[1], int(tokens[0]))
            loc.add_file(f)
    threshold = 30000000 - (70000000 - home.size)
    possible = list()
    q = deque()
    q.append(home)
    while q:
        l = q.pop()
        if l.size >= threshold:
            possible.append(l)
        q.extend(l.sub_dirs.values())
    return sorted(possible, key=lambda x: x.size)[0].size

if __name__ == '__main__':
    run_tests(part1, test_pairs_part1)
    print()
    vals = tokenise_input_file('2022/day7.txt')
    print(f'Part 1 answer: {part1(vals)}')
    print()
    run_tests(part2, test_pairs_part2)
    print()
    print(f'Part 2 answer: {part2(vals)}')
