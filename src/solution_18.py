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
    lines = utils.read_lines(input)
    coords = [(i.split(",")[0], i.split(",")[1]) for i in lines]
    grid = [["." for i in range(71)] for j in range(71)]
    for i in coords[0:1024]:
        grid[int(i[1])][int(i[0])] = "#"
    return utils.dijkstra_grid(grid, "#", (0,0), (70,70))[0]

def problem2(input: str) -> int | str:
    lines = utils.read_lines(input)
    coords = [(i.split(",")[0], i.split(",")[1]) for i in lines]
    grid = [["." for i in range(71)] for j in range(71)]
    out = 0
    for idx, i in enumerate(coords):
        print(idx)
        grid[int(i[1])][int(i[0])] = "#"
        if utils.dijkstra_grid(grid, "#", (0,0), (70,70))[0] == -1:
            out = i
            print("FOUND", i)
            break
        
    utils.print_grid(grid)
    return out
if __name__ == "__main__":
    input_path = utils.get_input_file(Path(__file__).resolve().parent / "data", 18)
    #print(problem1(input_path))
    print(problem2(input_path))