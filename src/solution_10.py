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


def problem1(input: str) -> int | str:
    output: int = 0
    grid = utils.parse_grid(utils.read_file(input))
    
    trailheads = []
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "0":
                trailheads.append((i, j))
    
    def can_find_peak(trailhead):
        # DFS
        visited = set()
        stack = [trailhead]
        num_nines = 0
        while stack:
            i, j = stack.pop()
            cur = int(grid[i][j])
            if (i, j) in visited:
                continue
            if cur == 9:
                num_nines += 1
                visited.add((i, j))
                continue
            visited.add((i, j))
            for neighbor in utils.get_neighbors(i, j, grid):
                ni, nj = neighbor
                if int(grid[ni][nj]) == cur + 1:
                    stack.append(neighbor)
        return num_nines
    
    for trailhead in trailheads:
        output += can_find_peak(trailhead)
            
    return output

def problem2(input: str) -> int | str:
    output: int = 0
    grid = utils.parse_grid(utils.read_file(input))
    
    trailheads = []
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "0":
                trailheads.append((i, j))
    
    def get_num_possible_trails_to_9_from_start(trailhead):
        # DFS
        current_trails = 0
        stack = [(trailhead, [], set())] # (position, path, visited)
        trails = []
        while stack:
            (i, j), path, visited = stack.pop()
            cur = int(grid[i][j])
            if (i, j) in visited:
                continue
            if cur == 9:
                current_trails += 1
                trails.append(path + [(i, j)])
                visited.add((i, j))
                continue
            visited.add((i, j))
            for neighbor in utils.get_neighbors(i, j, grid):
                ni, nj = neighbor
                if int(grid[ni][nj]) == cur + 1:
                    stack.append((neighbor, path + [(i, j)], visited.copy()))
        return len(trails)
            
    for trailhead in trailheads:
        output += get_num_possible_trails_to_9_from_start(trailhead)            

    return output


if __name__ == "__main__":
    input_path = utils.get_input_file(Path(__file__).resolve().parent / "data", 10)
    print(problem1(input_path))
    print(problem2(input_path))