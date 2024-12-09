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

    for i in re.findall(r"mul\(\d+\,\d+\)", f):
        i = i.replace('mul(','').replace(')','')
        output += int(i.split(',')[0])*int(i.split(',')[1])


    return output

def problem2(input: str) -> int | str:
    output: int = 0
    f = utils.read_file(input)
    # Add your solution logic here
    
    e = True

    for i in re.findall(r"(mul\(\d+\,\d+\))|(do\(\))|(don\'t\(\))", f):
        if i[2].find("don\'t") != -1:
            e = False
        elif i[1].find("do") != -1:
            e = True
        elif e:
            i = i[0].replace('mul(','').replace(')','')
            output += int(i.split(',')[0])*int(i.split(',')[1])

    return output

if __name__ == "__main__":
    input_path = utils.get_input_file(Path(__file__).resolve().parent / "data", 3)
    print(problem1(input_path))
    print(problem2(input_path))