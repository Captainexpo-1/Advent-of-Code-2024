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
    lines = utils.read_lines(input)
    
    l1 = []
    l2 = []
    for i in lines:
        i = i.split(" ")
        l1.append(int(i[0]))
        l2.append(int(i[-1]))
    
    l1 = sorted(l1)
    l2 = sorted(l2)

    d = 0
    for i,j in zip(l1, l2):
        d += abs(i - j)
        
    return d


def problem2(input: str) -> int | str:
    output: int = 0
    lines = utils.read_lines(input)
    
    l1 = []
    l2 = []
    for i in lines:
        i = i.split(" ")
        l1.append(int(i[0]))
        l2.append(int(i[-1]))
    
    l2 = collections.Counter(l2)

    for i in l1:
        output += i*l2[i]
        
    return output

if __name__ == "__main__":
    input_path = utils.get_input_file(Path(__file__).resolve().parent / "data", 1)
    print(problem1(input_path))
    print(problem2(input_path))
