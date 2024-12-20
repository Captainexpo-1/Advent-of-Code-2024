import sys
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# ---- imports ----
import AOC_Helpers as utils
from AOC_Helpers import lines
import re
import itertools
import collections
import math
import networkx
import numpy as np
import functools
from tqdm import tqdm

def problem1(input: str) -> int | str:
    f = utils.read_grid(input)
    
    start_pos = (0, 0)
    end_pos = (0, 0)
    
    for idx, row in enumerate(f):
        for jdx, col in enumerate(row):
            if col == "S":
                start_pos = (idx, jdx)
            if col == "E":
                end_pos = (idx, jdx)
    
    c = 0
    
    naive = utils.dijkstra_grid(f, "#", start_pos, end_pos)[1]
    for i in range(0, len(naive)):
        for j in range(i, len(naive)):
            x1,y1=naive[i]
            x2,y2=naive[j]
            
            if abs(x1-x2) + abs(y1-y2) <= 2 and abs(i-j) >= 100 + 2: # + 2 accounting for the movement between them 
                #print(x1,y1,x2,y2)
                c += 1
    return c
    

def problem2(input: str) -> int | str:
    f = utils.read_grid(input)
    
    start_pos = (0, 0)
    end_pos = (0, 0)
    
    for idx, row in enumerate(f):
        for jdx, col in enumerate(row):
            if col == "S":
                start_pos = (idx, jdx)
            if col == "E":
                end_pos = (idx, jdx)
    
    c = 0
    print(start_pos,end_pos)
    naive = utils.dijkstra_grid(f, "#", start_pos, end_pos)[1]
    for i in range(0, len(naive)):
        print(i, len(naive))
        for j in range(i, len(naive)):
            x1,y1=naive[i]
            x2,y2=naive[j]
            
            manhattan = abs(x1-x2) + abs(y1-y2)
            path_dist = j-i
            
            if manhattan <= 20 and path_dist >= 100 + manhattan: # + 2 accounting for the movement between them
                #print(x1,y1,x2,y2)
                c += 1
    return c
if __name__ == "__main__":
    sys.setrecursionlimit(300000)
    input_path = utils.get_input_file(Path(__file__).resolve().parent / "data", 20)
    #print(problem1(input_path))
    print(problem2(input_path))