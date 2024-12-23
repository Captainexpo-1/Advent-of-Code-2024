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
import matplotlib.pyplot as plt

def problem1(input: str) -> int | str:
    output: int = 0
    lines = utils.read_lines(input)


    G = networkx.Graph()  

    for line in lines:
        line = line.split('-')
        G.add_edge(line[0], line[1])
        G.add_edge(line[1], line[0])

        
    c = networkx.enumerate_all_cliques(G)
    
    m = []
    for k in c:
        if len(k) > len(m): m = k
    #print(cycles)
            
    return ','.join(sorted(m))

def problem2(input: str) -> int | str:
    output: int = 0
    lines = utils.read_lines(input)
    # Add your solution logic here
    
    return output

if __name__ == "__main__":
    input_path = utils.get_input_file(Path(__file__).resolve().parent / "data", 23)
    print(problem1(input_path))
    print(problem2(input_path))