import sys
import os
from pathlib import Path
from typing import Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# ---- imports ----
import AOC_Helpers as utils
import re
import itertools
import collections
import math
import networkx
from copy import deepcopy

def problem1(input: str) -> int | str:
    output: int = 0 
    grid = utils.parse_grid(utils.read_file(input))

    sims: dict[str, list[Tuple[int, int]]] = {}

    antinodes = [[0 for _ in i] for i in grid]
    
    
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == ".":
                continue
            if grid[y][x] not in sims:
                sims[grid[y][x]] = []
            sims[grid[y][x]].append((x, y))

    def is_in_bounds(x, y, grid):
        return x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid)

    for k, v in sims.items():
        for i in range(len(v)):
            for j in range(len(v)):
                if i == j:
                    continue
                dist: Tuple[int, int] = (v[j][0] - v[i][0], v[j][1] - v[i][1])
                if dist[0] == 0 and dist[1] == 0:
                    continue
                if is_in_bounds(v[i][0]-dist[0], v[i][1]-dist[1], grid):
                    antinodes[v[i][1]-dist[1]][v[i][0]-dist[0]] = 1
                if is_in_bounds(v[j][0]+dist[0], v[j][1]+dist[1], grid):
                    antinodes[v[j][1]+dist[1]][v[j][0]+dist[0]] = 1

    for y in range(len(antinodes)):
        for x in range(len(antinodes[y])):
            if antinodes[y][x] == 1:
                output += 1
                grid[y][x] = "#"
    
    for k in grid:
        print("".join(k))

    return output

from math import floor

def problem2(input: str) -> int | str:
    output: int = 0 
    grid = utils.parse_grid(utils.read_file(input))

    sims: dict[str, list[Tuple[int, int]]] = {}

    antinodes = [[0 for _ in i] for i in grid]
    
    
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == ".":
                continue
            if grid[y][x] not in sims:
                sims[grid[y][x]] = []
            sims[grid[y][x]].append((x, y))

    def is_in_bounds(x, y, grid):
        if floor(x) != x or floor(y) != y:
            return False
        return x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid)

    for k, v in sims.items():
        print(k,v)
        for i in range(len(v)):
            for j in range(len(v)):
                if i == j:
                    continue
                dist: Tuple[int, int] = (v[j][0] - v[i][0], v[j][1] - v[i][1])
                print(dist)
                for mul in itertools.count(0):
                    wow = (dist[0] * mul, dist[1] * mul)
                    fails = 0
                    if is_in_bounds(v[i][0]-wow[0], v[i][1]-wow[1], grid):
                        antinodes[v[i][1]-wow[1]][v[i][0]-wow[0]] = 1
                    else:
                        fails=1
                    if is_in_bounds(v[j][0]+wow[0], v[j][1]+wow[1], grid):
                        antinodes[v[j][1]+wow[1]][v[j][0]+wow[0]] = 1
                    elif fails:
                        break
    for y in range(len(antinodes)):
        for x in range(len(antinodes[y])):
            if antinodes[y][x] == 1:
                output += 1
                grid[y][x] = "#"


    return output

if __name__ == "__main__":
    input_path = utils.get_input_file(Path(__file__).resolve().parent / "data", 8)
    print(problem1(input_path))
    print(problem2(input_path))