import sys
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# ---- imports ----
import AOC_Helpers as utils
import re
import itertools
import collections
import math
import networkx
from copy import deepcopy

def find_path(grid: list[list[str]], start: complex) -> set[complex]:
    cur_pos = start
    dir = 0-1j
    path = {cur_pos: dir}

    def is_in_bounds(coord: complex):
        return coord.real >= 0 and coord.real < len(grid) and coord.imag >= 0 and coord.imag < len(grid[0])
    
    while is_in_bounds(cur_pos):
        next = cur_pos + dir
        if not is_in_bounds(next):
            path[cur_pos] = dir
            break
        if cur_pos in path and path[cur_pos] == dir:
            return "LOOP"
        if grid[int(next.imag)][int(next.real)] == "#":
            dir *= 0+1j
            path[cur_pos] = dir
            continue
        cur_pos = next
        path[cur_pos] = dir
    return path

def problem1(input: str) -> int | str:
    output: int = 0
    grid = utils.parse_grid(utils.read_file(input))
    print(grid)
    cur_pos = 0+0j
    d = 0+1j
    for idx, i in enumerate(grid):
        for jdx, j in enumerate(i):
            if j == "^":

                cur_pos = complex(jdx, idx)
                grid[idx][jdx] = "."
                break
    print(cur_pos)
    # Make sure it's in bounds
    path = set([cur_pos])
    dir = 0-1j
    
    def is_in_bounds(coord: complex):
        return coord.real >= 0 and coord.real < len(grid) and coord.imag >= 0 and coord.imag < len(grid[0])
    while is_in_bounds(cur_pos):
        next = cur_pos + dir
        if not is_in_bounds(next):
            path.add(cur_pos)
            break
        if grid[int(next.imag)][int(next.real)] == "#":
            dir *= 0+1j
            path.add(cur_pos)
            continue
        #grid[int(cur_pos.imag)][int(cur_pos.real)] = "X"
        cur_pos = next
        
        path.add(cur_pos)

    # Add your solution logic here
    print(path)
    return len(path)


def problem2(input: str) -> int | str:
    output: int = 0
    grid = utils.parse_grid(utils.read_file(input))
    print(grid)
    cur_pos = 0+0j
    d = 0+1j
    for idx, i in enumerate(grid):
        for jdx, j in enumerate(i):
            if j == "^":

                cur_pos = complex(jdx, idx)
                grid[idx][jdx] = "."
                break
    print(cur_pos)
    # Make sure it's in bounds
    path = {cur_pos: set([d])}
    dir = 0-1j
    
    def is_in_bounds(coord: complex):
        return coord.real >= 0 and coord.real < len(grid) and coord.imag >= 0 and coord.imag < len(grid[0])
    
    while is_in_bounds(cur_pos):
        next = cur_pos + dir
        if not is_in_bounds(next):
            path.setdefault(cur_pos, set())
            path[cur_pos].add(dir)
            break
        if grid[int(next.imag)][int(next.real)] == "#":
            dir *= 0+1j
            path.setdefault(cur_pos, set())
            path[cur_pos].add(dir)
            continue
        #grid[int(cur_pos.imag)][int(cur_pos.real)] = "X"
        cur_pos = next
        
        path.setdefault(cur_pos, set())
        path[cur_pos].add(dir)
    
    for pos, dirs in path.items():
        for dir in dirs:
            new_grid = deepcopy(grid)
            next = pos + dir
            if not is_in_bounds(next): continue
            if new_grid[int(next.imag)][int(next.real)] == "#": continue
            
            new_grid[int(next.imag)][int(next.real)] = "#"
            new_path = find_path(new_grid, pos)
            if new_path == "LOOP":
                output += 1
                print("LOOP")
                continue
            print(new_path)

    # Add your solution logic here
    return output

if __name__ == "__main__":
    input_path = utils.get_input_file(Path(__file__).resolve().parent / "data", 6)
    print(problem1("O:/Documents/vscode/AOC2024/src/data/input_06.txt"))
    print(problem2(input_path))
    