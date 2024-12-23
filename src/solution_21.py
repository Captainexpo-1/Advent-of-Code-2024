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

def problem1(input: str) -> int | str:
    ROBOT_COUNT = 2

    keypad_paths = [
        ['7', '8', '9'],
        ['4', '5', '6'],
        ['1', '2', '3'],
        [' ', '0', 'A']
    ]

    dirpad_paths = [
        [' ' , '^', 'A'],
        ['<', 'v', '>'],
    ]

    def get_paths(grid):
        G = networkx.DiGraph()
        for i, row in enumerate(grid):
            for j, key in enumerate(row):
                if key == ' ':
                    continue  
                G.add_node(key, pos=(i,j))   
                for di, dj, direction in [(0,1,'>'), (0,-1,'<'), (1,0,'v'), (-1,0,'^')]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < len(grid) and 0 <= nj < len(row) and grid[ni][nj] != ' ':
                        G.add_edge(key, grid[ni][nj], direction=direction)

        # Find all shortest paths
        paths = collections.defaultdict(list)
        for start in G.nodes():
            for end in G.nodes():
                if start != end:
                    raw_paths = list(networkx.all_shortest_paths(G, start, end))
                    for path in raw_paths:
                        directions = [ G[path[i]][path[i+1]]['direction'] for i in range(len(path)-1)]
                        paths[(start, end)].append(''.join(directions))

        return paths

    @functools.cache
    def min_robot_path(level, text):
        if level == ROBOT_COUNT + 1:
            return len(text)
        all_paths = keypad if level == 0 else dirpad
        k_total = 0
        for start, end in zip('A'+text, text):
            minks = [ min_robot_path(level+1, path + 'A') for path in all_paths[(start, end)]]
            minks = [ k for k in minks if k is not None]
            k_total += min(minks) if minks else 1
        return k_total


    keypad = get_paths(keypad_paths)
    dirpad = get_paths(dirpad_paths)
    total = 0
    for code in utils.read_lines(input):
        ordinal = int("".join([c for c in code if c.isdigit()]))
        min_len = min_robot_path(0, code)
        total += ordinal * min_len
    return total
    
def problem2(input: str) -> int | str:
    ROBOT_COUNT = 25

    keypad_paths = [
        ['7', '8', '9'],
        ['4', '5', '6'],
        ['1', '2', '3'],
        [' ', '0', 'A']
    ]

    dirpad_paths = [
        [' ' , '^', 'A'],
        ['<', 'v', '>'],
    ]

    def get_paths(grid):
        G = networkx.DiGraph()
        for i, row in enumerate(grid):
            for j, key in enumerate(row):
                if key == ' ':
                    continue  
                G.add_node(key, pos=(i,j))   
                for di, dj, direction in [(0,1,'>'), (0,-1,'<'), (1,0,'v'), (-1,0,'^')]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < len(grid) and 0 <= nj < len(row) and grid[ni][nj] != ' ':
                        G.add_edge(key, grid[ni][nj], direction=direction)

        # Find all shortest paths
        paths = collections.defaultdict(list)
        for start in G.nodes():
            for end in G.nodes():
                if start != end:
                    raw_paths = list(networkx.all_shortest_paths(G, start, end))
                    for path in raw_paths:
                        directions = [ G[path[i]][path[i+1]]['direction'] for i in range(len(path)-1)]
                        paths[(start, end)].append(''.join(directions))

        return paths

    @functools.cache
    def min_robot_path(level, text):
        if level == ROBOT_COUNT + 1:
            return len(text)
        all_paths = keypad if level == 0 else dirpad
        k_total = 0
        for start, end in zip('A'+text, text):
            minks = [ min_robot_path(level+1, path + 'A') for path in all_paths[(start, end)]]
            minks = [ k for k in minks if k is not None]
            k_total += min(minks) if minks else 1
        return k_total


    keypad = get_paths(keypad_paths)
    dirpad = get_paths(dirpad_paths)
    total = 0
    for code in utils.read_lines(input):
        ordinal = int("".join([c for c in code if c.isdigit()]))
        min_len = min_robot_path(0, code)
        total += ordinal * min_len
    return total

if __name__ == "__main__":
    input_path = utils.get_input_file(Path(__file__).resolve().parent / "data", 21)
    print(problem1(input_path))
    print(problem2(input_path))