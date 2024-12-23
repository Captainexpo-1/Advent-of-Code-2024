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
from pprint import pprint
import json

def precalculate_paths(keypad, dirpad):
    # make a graph out of the keypad using networkx
    G_keypad = networkx.Graph()
    for k,v in keypad.items():
        G_keypad.add_node(v)
    for k1,v1 in keypad.items():
        for k2, v2 in keypad.items():
            if k1 == k2: continue
            if abs(v1-v2) == 1 or abs(v1-v2) == 1j:
                G_keypad.add_edge(v1,v2)
    
    G_dirpad = networkx.Graph()
    for k,v in dirpad.items():
        G_dirpad.add_node(v)
    for k1,v1 in dirpad.items():
        for k2, v2 in dirpad.items():
            if k1 == k2: continue
            if abs(v1-v2) == 1 or abs(v1-v2) == 1j:
                G_dirpad.add_edge(v1,v2)
                
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

            x = ''.join(list(get_path_as_chrs(path)))
            
            keypad_shortest_paths[k1][k2] = x
        keypad_shortest_paths[k1][k1] = ""
        
    dirpad_shortest_paths = collections.defaultdict(dict)
    for k1,v1 in dirpad.items():
        for k2, v2 in dirpad.items():
            if k1 == k2: continue
            path = networkx.shortest_path(G_dirpad, v1, v2)
            
            x = ''.join(list(get_path_as_chrs(path)))
            
            
            dirpad_shortest_paths[k1][k2] = x
        dirpad_shortest_paths[k1][k1] = ""
    
    return dict({k:dict(v) for k,v  in keypad_shortest_paths.items()}), dict(dirpad_shortest_paths)

def problem1(input: str) -> int | str:
    lines = utils.read_lines(input)
    
    keypad = {
        '7': 0+0j,'8': 1+0j,'9': 2+0j,
        '4': 0+1j,'5': 1+1j,'6': 2+1j,
        '1': 0+2j,'2': 1+2j,'3': 2+2j,
                  '0': 1+3j,'A': 2+3j,
    }
    
    #<A^A>^^AvvvA
    dirpad = {
                   '^': 1+0j, 'A': 2+0j,
        '<': 0+1j, 'v': 1+1j, '>': 2+1j,
    }


    
    #keypad_shortest_paths, dirpad_shortest_paths = precalculate_paths(keypad, dirpad)


    keypad_shortest_paths = {
        "7": {
            "8": ">",
            "9": ">>",
            "4": "v",
            "5": "v>",
            "6": "v>>",
            "1": "vv",
            "2": "vv>",
            "3": "vv>>",
            "0": "vvv>",
            "A": "vvv>>",
            "7": ""
        },
        "8": {
            "7": "<",
            "9": ">",
            "4": "<v",
            "5": "v",
            "6": "v>",
            "1": "<vv",
            "2": "vv",
            "3": "vv>",
            "0": "vvv",
            "A": "vvv>",
            "8": ""
        },
        "9": {
            "7": "<<",
            "8": "<",
            "4": "<<v",
            "5": "<v",
            "6": "v",
            "1": "<<vv",
            "2": "<vv",
            "3": "vv",
            "0": "<vvv",
            "A": "vvv",
            "9": ""
        },
        "4": {
            "7": "^",
            "8": "^>",
            "9": "^>>",
            "5": ">",
            "6": ">>",
            "1": "v",
            "2": "v>",
            "3": "v>>",
            "0": "vv>",
            "A": "vv>>",
            "4": ""
        },
        "5": {
            "7": "<^",
            "8": "^",
            "9": "^>",
            "4": "<",
            "6": ">",
            "1": "<v",
            "2": "v",
            "3": "v>",
            "0": "vv",
            "A": "vv>",
            "5": ""
        },
        "6": {
            "7": "<<^",
            "8": "<^",
            "9": "^",
            "4": "<<",
            "5": "<",
            "1": "<<v",
            "2": "<v",
            "3": "v",
            "0": "<vv",
            "A": "vv",
            "6": ""
        },
        "1": {
            "7": "^^",
            "8": "^^>",
            "9": "^^>>",
            "4": "^",
            "5": "^>",
            "6": "^>>",
            "2": ">",
            "3": ">>",
            "0": "v>",
            "A": "v>>",
            "1": ""
        },
        "2": {
            "7": "<^^",
            "8": "^^",
            "9": "^^>",
            "4": "<^",
            "5": "^",
            "6": "^>",
            "1": "<",
            "3": ">",
            "0": "v",
            "A": "v>",
            "2": ""
        },
        "3": {
            "7": "<<^^",
            "8": "<^^",
            "9": "^^",
            "4": "<<^",
            "5": "<^",
            "6": "^",
            "1": "<<",
            "2": "<",
            "0": "<v",
            "A": "v",
            "3": ""
        },
        "0": {
            "7": "^^^<",
            "8": "^^^",
            "9": "^^^>",
            "4": "^^<",
            "5": "^^",
            "6": "^^>",
            "1": "^<",
            "2": "^",
            "3": "^>",
            "A": ">",
            "0": ""
        },
        "A": {
            "7": "^^^<<",
            "8": "<^^^",
            "9": "^^^",
            "4": "^^<<",
            "5": "<^^",
            "6": "^^",
            "1": "^<<",
            "2": "<^",
            "3": "^",
            "0": "<",
            "A": ""
        }
    }
    # <v^>
    dirpad_shortest_paths = {
        "^": {
            "A": ">",
            "<": "<v",
            "v": "v",
            ">": "v>",
            "^": ""
        },
        "A": {
            "^": "<",
            "<": "v<<",
            "v": "<v",
            ">": "v",
            "A": ""
        },
        "<": {
            "^": ">^",
            "A": ">>^",
            "v": ">",
            ">": ">>",
            "<": ""
        },
        "v": {
            "^": "^",
            "A": "^>",
            "<": "<",
            ">": ">",
            "v": ""
        },
        ">": {
            "^": "<^",
            "A": "^",
            "<": "<<",
            "v": "<",
            ">": ""
        }
    }




    def get_robot_output(robot_num, cur_path):
        if robot_num == 3:
            return cur_path
        paths = dirpad_shortest_paths if robot_num > 0 else keypad_shortest_paths
        
        path = ""
        for start, end in zip("A"+cur_path, cur_path):
            #print(start, end, paths[start][end])
            path += paths[start][end]+"A"
        
        return get_robot_output(robot_num+1, path)
        # get shortest path
        
    
    complexities = 0
    for line in lines:
       result = get_robot_output(0, line)
       complexities += len(result) * int(line[:-1].lstrip('0'))
       print(line, result)
       
#^A<<^^A>>AvvvA
       
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