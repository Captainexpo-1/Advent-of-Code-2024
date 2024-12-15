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
    f = utils.read_file(input).split("\n\n")
    grid = utils.parse_grid(f[0])
    dirs = list(f[1].replace("\n",""))
    robot_pos = (0,0)
    
    for idx, i in enumerate(grid):
        for jdx, j in enumerate(i):
            if j == "@":
                robot_pos = (jdx, idx)
                break
    
    def try_do_move(x, y, dx, dy):
        current = grid[y][x]
        #print(current)
        if current == "#": return False
        if current == ".": return True
        if current == "@":
            # try move robot
            if try_do_move(x+dx, y+dy, dx, dy):
                grid[y+dy][x+dx] = "@"
                grid[y][x] = "."
                return (x+dx, y+dy)
            return False
        if current == "O": 
            # try move box
            if try_do_move(x+dx, y+dy, dx, dy):
                grid[y+dy][x+dx] = "O"
                grid[y][x] = "."
                return True
            return False
        return False
    
    for d in dirs:
        match d:
            case "^":
                l = (0,-1)
            case "v":
                l = (0,1)
            case ">":
                l = (1,0)
            case "<":
                l = (-1,0)
            case _:
                print(f'"{d}"')
                raise Exception("WAHHH")
        m = try_do_move(robot_pos[0], robot_pos[1], l[0], l[1])
        if isinstance(m, tuple):
            robot_pos = m
    for idx, i in enumerate(grid):
        for jdx, j in enumerate(i):
            if j == "O":
                output += 100*idx + jdx
        
    
    
    # Add your solution logic here
    
    return output

def problem2(file: str) -> int | str:
    output: int = 0
    f = utils.read_file(file).split("\n\n")
    grid = utils.parse_grid(f[0])
    new_grid = []
    dirs = list(f[1].replace("\n",""))
    robot_pos = (0,0)
    
    for idx, i in enumerate(grid):
        row = []
        for jdx, j in enumerate(i):
            if j == "@":
                row.extend("@.")
            elif j == "O":
                row.extend("[]")
            elif j == "#":
                row.extend("##")
            elif j == ".":
                row.extend("..")
        new_grid.append(row)
    
    grid = new_grid
    
    for idx, i in enumerate(grid):
        for jdx, j in enumerate(i):
            if j == "@":
                robot_pos = (jdx, idx)
                break
    for row in grid:
        print(''.join(row))
                
    def try_do_move(x, y, dx, dy, is_companion=False, is_companion_check=False, do_is_companion_check=True, is_searching=False):
        current = grid[y][x]    
        if current == "#": return False
        if current == ".": return True
        if current == "@":
            # try move robot
            if try_do_move(x+dx, y+dy, dx, dy):
                grid[y+dy][x+dx] = "@"
                grid[y][x] = "."
                return (x+dx, y+dy)
            return False

        if current in "[]" and dy != 0: 
            # try move box
            if is_companion:
                #print(current,x,y)
                if try_do_move(x+dx, y+dy, dx, dy, is_companion_check=(True and do_is_companion_check)):
                    if not do_is_companion_check and not is_searching:
                        grid[y+dy][x+dx] = current
                        grid[y][x] = "."
                    return True
                return False
            
            companion = (x+1,y) if current == "[" else (x-1,y)
            if try_do_move(companion[0], companion[1], dx, dy, is_companion=True, is_searching=True) and try_do_move(x+dx, y+dy, dx, dy, is_searching=True):
                if not is_companion_check and not is_searching:
                    try_do_move(companion[0], companion[1], dx, dy, is_companion=True, do_is_companion_check=False)
                    try_do_move(x, y, dx, dy, is_companion=True, do_is_companion_check=False)
                    #grid[y+dy][x+dx] = current
                    #grid[y][x] = "."

                return True
            return False
        elif dy == 0:
            next = grid[y+dy][x+dx]
            if next == ".":
                grid[y+dy][x+dx] = current
                grid[y][x] = "."
                return True
            if try_do_move(x+dx, y+dy, dx, dy):
                grid[y+dy][x+dx] = current
                grid[y][x] = "."
                return True
        return False
    #b = 0
    #test = 367
    for d in dirs:
        #print(d)
        match d:
            case "^":
                l = (0,-1)
            case "v":
                l = (0,1)
            case ">":
                l = (1,0)
            case "<":
                l = (-1,0)
            case _:
                print(f's"{d}"')
                raise Exception("WAHHH")
        m = try_do_move(robot_pos[0], robot_pos[1], l[0], l[1])
        output = 0
        for idx, i in enumerate(grid):
            for jdx, j in enumerate(i[:-1]):
                if grid[idx][jdx]+grid[idx][jdx+1] == "[]":
                    # found box
                    output += idx*100 + jdx
        if isinstance(m, tuple):
            robot_pos = m
            
          
    output = 0
    for idx, i in enumerate(grid):
        for jdx, j in enumerate(i[:-1]):
            if grid[idx][jdx]+grid[idx][jdx+1] == "[]":
                # found box
                output += idx*100 + jdx
                
    return output

if __name__ == "__main__":
    input_path = utils.get_input_file(Path(__file__).resolve().parent / "data", 15)
    #print(problem1(input_path))
    print(problem2(input_path))