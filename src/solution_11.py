import sys
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# ---- imports ----
import AOC_Helpers as utils
import re
import itertools, functools
import collections
import math
import networkx
import queue

def problem1(input: str) -> int | str:
    output: int = 0
    f = utils.read_file(input)
    
    stones = [int(x) for x in f.split(" ")]
    
    for iter in range(75):
        idx = len(stones)-1
        while idx >= 0:
            s = stones[idx]
            if s == 0:
                stones[idx] = 1
            elif len(str(s)) % 2 == 0:
                stones[idx] = int(str(s)[len(str(s))//2:])
                stones.insert(idx, int(str(s)[:len(str(s))//2]))
            else:
                stones[idx] = s*2024
            idx -= 1
        
        
    return len(stones)


def problem2(input: str) -> int | str:
    f = utils.read_file(input)
    
    _stones = [int(x) for x in f.split(" ")]
    
    @functools.cache
    def recurse(iter, stone):
        if iter == 0:
            return 1
        
        if stone == 0:
            return recurse(iter-1, 1)
        
        s_str = str(stone)
        n = len(s_str)
        
        if n % 2 == 0:
            a = int(s_str[:n//2])
            b = int(s_str[n//2:])
            return (
                recurse(iter-1, a) + 
                recurse(iter-1, b)
            )
        return recurse(iter-1, stone*2024)

    return sum([recurse(75, i) for i in _stones])
        


if __name__ == "__main__":
    sys.setrecursionlimit(999999999)
    input_path = utils.get_input_file(Path(__file__).resolve().parent / "data", 11)
    #print(problem1(input_path))
    print(problem2(input_path))