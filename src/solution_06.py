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
from copy import deepcopy

def find_path(grid: list[list[str]], start: complex) -> set[complex]:
    cur_pos = start
    dir = 0-1j
    path = {}

    if grid[int(cur_pos.imag)][int(cur_pos.real)] == "#": return path.keys()

    def is_in_bounds(coord: complex):
        return coord.real >= 0 and coord.real < len(grid) and coord.imag >= 0 and coord.imag < len(grid[0])
    
    while is_in_bounds(cur_pos):
        #print(cur_pos, path.get(cur_pos))
        # Return "LOOP" if we've already visited this position while going in the same direction
        if cur_pos in path and dir in path[cur_pos]:
            return True
        path.setdefault(cur_pos, set())
        path[cur_pos].add(dir)
        next = cur_pos + dir
        if not is_in_bounds(next):
            return path.keys()
        if grid[int(next.imag)][int(next.real)] == "#":
            dir *= 0+1j
            continue
        cur_pos = next
    return path.keys()

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
    for idx, i in enumerate(grid):
        for jdx, j in enumerate(i):
            if j == "^":

                cur_pos = complex(jdx, idx)
                grid[idx][jdx] = "."
                break
    print(cur_pos)
    
    p = find_path(grid, cur_pos)

    for idx in range(0, len(grid)):
        for jdx in range(0,len(grid[0])):
            # Prevent the wall from spawning on the start position
            if complex(jdx, idx) not in p: continue
            new_grid = deepcopy(grid)
            new_grid[idx][jdx] = "#"
            #print(new_grid[int(cur_pos.imag)][int(cur_pos.real)], cur_pos, idx, jdx)
            path = find_path(new_grid, cur_pos)
            print(f"{idx*len(grid[0])+jdx}/{len(grid)*len(grid[0])}, out={output}")
            if path == True:
                output += 1
                

    # Add your solution logic here
    print()
    return "Result:",output

if __name__ == "__main__":
    input_path = utils.get_input_file(Path(__file__).resolve().parent / "data", 6)
    print(problem1(input_path))
    print(problem2(input_path))
    