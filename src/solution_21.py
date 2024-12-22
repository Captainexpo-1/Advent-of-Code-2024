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
import functools

def problem1(input: str) -> int | str:
    lines = utils.read_lines(input)
    
    keypad = {
        '7': 0+0j,'8': 1+0j,'9': 2+0j,
        '4': 0+1j,'5': 1+1j,'6': 2+1j,
        '1': 0+2j,'2': 1+2j,'3': 2+2j,
                  '0': 1+3j,'A': 2+3j,
    }
    
    # make a graph out of the keypad using networkx
    G_keypad = networkx.DiGraph()
    for k,v in keypad.items():
        G_keypad.add_node(v)
    for k1,v1 in keypad.items():
        for k2, v2 in keypad.items():
            if k1 == k2: continue
            if abs(v1-v2) == 1 or abs(v1-v2) == 1j:
                G_keypad.add_edge(v1,v2)
    
    dirpad = {
                   '^': 1+0j, 'A': 2+0j,
        '<': 0+1j, 'v': 1+1j, '>': 2+1j,
    }
    
    G_dirpad = networkx.Graph()
    for k,v in dirpad.items():
        G_dirpad.add_node(v)
    for k1,v1 in dirpad.items():
        for k2, v2 in dirpad.items():
            if k1 == k2: continue
            if abs(v1-v2) == 1 or abs(v1-v2) == 1j:
                G_dirpad.add_edge(v1,v2)
    
    #print(G_dirpad.edges)
    #print(G_keypad.edges)
    
    def get_path_as_chrs(path: list):
        for idx in range(len(path)-1):
            diff = path[idx+1] - path[idx]
            if   diff ==   1: yield '>'
            elif diff ==  -1: yield '<'
            elif diff ==  1j: yield 'v'
            elif diff == -1j: yield '^'

    keypad_shortest_paths = collections.defaultdict(collections.defaultdict[list])
    for k1,v1 in keypad.items():
        for k2, v2 in keypad.items():
            if k1 == k2: continue
            path = networkx.shortest_path(G_keypad, v1, v2)
            keypad_shortest_paths[k1][k2] = [''.join(i) for i in itertools.permutations(''.join(list(get_path_as_chrs(path))))]
        keypad_shortest_paths[k1][k1] = 'A'
        
    dirpad_shortest_paths = collections.defaultdict(dict)
    for k1,v1 in dirpad.items():
        for k2, v2 in dirpad.items():
            if k1 == k2: continue
            path = networkx.shortest_path(G_dirpad, v1, v2)
            dirpad_shortest_paths[k1][k2] = [''.join(i) for i in itertools.permutations(''.join(list(get_path_as_chrs(path))))]
        dirpad_shortest_paths[k1][k1] = 'A'
    
    #print(dirpad_shortest_paths)
    
    @functools.cache
    def get_robot_output(inp, robot):
        shortest_paths = dirpad_shortest_paths
        if robot == 1:
            return inp
        if robot == 0:
            shortest_paths = keypad_shortest_paths
        
        pos = 'A'
        
        chunks = ["" for i in range(len(inp))]
 
        for chunk_idx in range(len(chunks)):
            i = inp[chunk_idx]
            min_new_chunk = ""
            min_new_len = math.inf
            #print(pos, shortest_paths[pos], i, shortest_paths[pos].get(i))
            for path in shortest_paths[pos][i]:
                p = get_robot_output(path+"A", robot+1)
                if len(p) < min_new_len:
                    min_new_len = len(p)
                    min_new_chunk = path+"A"
            chunks[chunk_idx] = min_new_chunk

            pos = i
        
        return get_robot_output(''.join(chunks), robot+1)
    complexities = 0
    for line in lines:
       result = get_robot_output(line, 0)
       complexities += len(result) * int(line[:-1].lstrip('0'))
       print(line, result)
    return complexities
    
def problem2(input: str) -> int | str:
    output: int = 0
    lines = utils.read_lines(input)
    # Add your solution logic here
    
    return output

if __name__ == "__main__":
    input_path = utils.get_input_file(Path(__file__).resolve().parent / "data", 21)
    print(problem1(input_path))
    print(problem2(input_path))