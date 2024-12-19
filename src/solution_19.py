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
    f = utils.read_file(input)
    
    patterns,designs = f.split("\n\n")
    
    designs=designs.split("\n")
    patterns=set(patterns.split(", "))
    print(designs, patterns)
    
    def design_is_possible(design: str) -> bool:
        cache = set()
        def dfs(cur_design: str, design: str, patterns: set[str]) -> bool:
            if cur_design in cache:
                return False
            if cur_design == design:
                return True
            if len(cur_design) >= len(design):
                cache.add(cur_design)
                return False
            for pattern in patterns:
                if design.startswith(cur_design + pattern):
                    if dfs(cur_design + pattern, design, patterns):
                        return True
            cache.add(cur_design)
            return False
        
        return dfs("", design, patterns)
        
    for design in designs:
        if design_is_possible(design):
            output += 1
        else:
            print(design)
    return output

def problem2(input: str) -> int | str:
    output: int = 0
    f = utils.read_file(input)
    
    patterns,designs = f.split("\n\n")
    
    designs=designs.split("\n")
    patterns=set(patterns.split(", "))
    print(designs, patterns)
    
    def design_is_possible(design: str) -> bool:
        cache = {}
        def dfs(cur_design: str, design: str, patterns: set[str]) -> bool:
            if cur_design in cache:
                return cache[cur_design]
            if cur_design == design:
                cache[cur_design] = 1
                return 1
            if len(cur_design) >= len(design):
                cache[cur_design] = False
                return False
            trues = 0
            for pattern in patterns:
                if design.startswith(cur_design + pattern):
                    res = dfs(cur_design + pattern, design, patterns)
                    if res: trues += res
            if trues >= 1:
                cache[cur_design] = trues
                return trues
            cache[cur_design] = False
            return False
        
        return dfs("", design, patterns)

    i = 0
    for design in designs:
        print(i)
        output += design_is_possible(design)
        i += 1
    return output


if __name__ == "__main__":
    input_path = utils.get_input_file(Path(__file__).resolve().parent / "data", 19)
    print(problem1(input_path))
    print(problem2(input_path))