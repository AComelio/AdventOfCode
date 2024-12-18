# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 09:25:46 2020
@author: Adam.Comelio
"""

import time
from itertools import product
import requests
import os
from environment import session_token

def time_me(func):
    def inner1(*args, **kwargs):
        st = time.perf_counter_ns()
        r = func(*args, **kwargs)
        print('Function done in {} seconds real time'.format(
                                            (time.perf_counter_ns()-st)/1e9))
        return r
    return inner1

def tokenise_input_file(src, seperator='\n', func=None):
    if os.path.exists(src):
        filepath = src
        with open(filepath, 'r') as f:
            text = f.read()
    else:
        text = src
    if func is None:
        return text.split(seperator)
    return tuple(map(func, text.split(seperator)))

def run_tests(func, io_pairs):
    print(f'Running {len(io_pairs)} test(s)')
    for i, (func_input, correct_output) in enumerate(io_pairs):
        result = func(func_input)
        if result == correct_output:
            print(f'Test {i+1} passed')
        else:
            print(f'Test {i+1} failed, output was {result}')
    print('Tests done')

def get_adjacent_coords(coord, include_self=False):
    difs = (-1,0,1)
    ranges = tuple(tuple(map(lambda x: x + v, difs)) for v in coord)
    if include_self:
        return tuple(product(*ranges))
    return tuple(p for p in product(*ranges) if p != coord)

def request_problem_input(day, year):
    fp = f'day{day}_input.txt'
    if not os.path.exists(fp):
        uri = f'https://adventofcode.com/{year}/day/{day}/input'
        response = requests.get(uri, cookies={'session': session_token})
        with open(fp, 'w') as f:
            f.write(response.text)
    with open(fp, 'r') as f:
        inputs = f.read()
    return inputs.strip()
