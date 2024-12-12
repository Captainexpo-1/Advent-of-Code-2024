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
    """
    The problem is that it only counts distances against the ones with the same depth, not all of them
    That means that the sides are not counted correctly, e.g. 
    
    4 [[8, 9, 7, 7, 8]]
    4 [[6, 5, 6], [9]]
    2 [[1, 0, 0, 0, 0]]
    3 [[0, 0, 2], [2]] <- 2 sides b/c of 2 different consecutive depths, could be fixed with some tuple magic
    F 10 * 13 = 130
    RRRRIICC**
    RRRRIICCC*
    VVRRRCC***
    VVRCCCJ***
    VVVVCJJC*E
    VVIVCCJJEE
    VVIIICJJEE
    MIIIIIJJEE
    MIIISIJEEE
    MMMISSJEEE
    
    """
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
            # side data struct = list of dicts {init_pos: (x, y), direction: (dx, dy)} where dir is the direction pointing out of the shape
            
            # top to down, left to right traversal to find top borders
            def cast_ray_get_dist(y):
                x = 0
                hits = []
                while x < len(filled[0]):
                    if filled[y][x] == "*":
                        if x == 0 or filled[y][x-1] != "*":
                            hits.append(x)
                    x += 1
                return hits
            
            sides = 0
            for _ in range(4):
                distances_per_penetration = [] # list of lists of distances for each pendepth idx = # pens, val = distance
                for y in range(len(filled)):
                    d = cast_ray_get_dist(y) # r
                    if len(d) == 0:
                        continue
                    for i in range(len(d)):
                        if len(distances_per_penetration) <= i:
                            distances_per_penetration.append([])
                        distances_per_penetration[i].append(d[i])
                #print(distances_per_penetration)
                
                def get_sides(distances):
                    if len(distances) == 0:
                        return 0
                    else:
                        s = 1
                    for i in range(1, len(distances)):
                        if distances[i] != distances[i-1]: 
                            s += 1
                    return s
                t=0
                for pens in distances_per_penetration:
                    m =get_sides(pens)
                    #print(pens,"D PER P", m)
                    t += m
                print(t, distances_per_penetration, )
                sides += t
                filled = utils.rotate_90_degrees(filled)
            #print(cur_val, sides)                
            output += len(filled_positions) * sides
            print(cur_val, len(filled_positions),"*",sides,"=",len(filled_positions) * sides)
            #filled = utils.rotate_90_degrees(filled)
            for row in filled:
                print("".join(row))
            all_filled.update(filled_positions)
            j += 1
            #print(i)
        i += 1
    return output

if __name__ == "__main__":
    input_path = utils.get_input_file(Path(__file__).resolve().parent / "data", 12)
    print(problem1(input_path))
    print(problem2(input_path))