import sys
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# ---- imports ----
import AOC_Helpers as utils
import re
import itertools
import collections
import functools
import math
import networkx
from copy import deepcopy


def problem1(input: str) -> int | str:
    output: int = 0
    f = utils.read_file(input)
    grid = utils.parse_grid(f)

    
    i = 0
    all_filled = set()
    while i < len(grid):
        j = 0
        while j < len(grid[i]):
            if (i, j) in all_filled:
                j += 1
                continue
            cur_val = grid[i][j]
            #print(cur_val)
            filled, filled_positions = utils.flood_fill(grid, empty_val=cur_val, use_inside=True, inside_pos=(i,j), fill_val="*")
            #for row in filled:
                #print("".join(row))
            perim = 0
            for x, y in filled_positions:
                
                #print("\n",x, y)
                n = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
                for l in (n:=utils.get_neighbors(x, y, filled)):
                    if l not in filled_positions:
                        perim += 1
                    
                        #print(filled[l[1]][l[0]],end=",")
                    #print(filled[l[1]][l[0]],end=",")
            # add perimeter to output
            output += perim * len(filled_positions)
            #print(cur_val, perim,"*",len(filled_positions))
            all_filled.update(filled_positions)
            j += 1
        i += 1
        
            

    return output

def problem2(input: str) -> int | str:
    output: int = 0
    f = utils.read_file(input)
    grid = utils.parse_grid(f)

    
    i = 0
    all_filled = set()
    while i < len(grid):
        j = 0

        while j < len(grid[i]):
            if (i, j) in all_filled:
                j += 1
                continue
            cur_val = grid[i][j]
            filled, filled_positions = utils.flood_fill(grid, empty_val=cur_val, use_inside=True, inside_pos=(i,j), fill_val="*")
            
            filled = [["%" for _ in range(len(filled[0]))]] + filled + [["%" for _ in range(len(filled[0]))]]
            for idx in range(len(filled)):
                filled[idx] = ["%"] + filled[idx] + ["%"]
                
            # get number of contiguous sides of the shape
            
            data = deepcopy(filled)
            
            for y in range(len(filled)):
                for x in range(len(filled[y])):
                    data[y][x] = []
                    if filled[y][x] != "*":
                        for x1,y1 in utils.get_neighbors(x, y, data):
                            if filled[y1][x1] == "*":
                                data[y][x].append((x-x1, y-y1))
                                #filled[y][x] = "#"
                        
            #utils.print_grid(filled)
            #print()
            def remove_all(x, y, to_remove: tuple[int, int]):
                nonlocal data
                #print(x, y, to_remove, data[y][x], to_remove in data[y][x])
                if to_remove not in data[y][x]:
                    return
                data[y][x].remove(to_remove)
                for x1, y1 in utils.get_neighbors(x, y, data):
                    remove_all(x1, y1, to_remove)
                
            
            sides = 0
            y = 0
            while y < len(data):
                x = 0
                while x < len(data[y]):
                    #print(x, y, data[y][x])
                    while data[y][x]:
                        o = data[y][x][0]
                        remove_all(x, y, o)
                        sides += 1 
                    x += 1
                y += 1
            output += sides * len(filled_positions)
            print(cur_val, sides, "*", len(filled_positions))
            all_filled.update(filled_positions)
            j += 1
        i += 1
    return output

if __name__ == "__main__":
    
    input_path = utils.get_input_file(Path(__file__).resolve().parent / "data", 12)
    print(problem1(input_path))
    print(problem2(input_path))