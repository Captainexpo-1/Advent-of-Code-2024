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
    lines = utils.read_lines(input)
    for i in lines:
        l = [int(j) for j in i.split(" ")]
        inc = l[0] < l[1]
        good = True
        last = l[0]
        for m in l[1:]:
            if m < last and inc: 
                good = False
                break
            elif inc == False and m > last:
                good = False
                break
            if not (abs(last-m) > 0 and abs(last-m) <= 3):
                good = False
                break
            last = m
        output += 1 if good else 0
    return output

def problem2(input: str) -> int | str:
    output: int = 0
    lines = utils.read_lines(input)
    for i in lines:
        l = [int(j) for j in i.split(" ")]
        def check(l):
            inc = l[0] < l[1]
            good = True
            last = l[0]
            for m in l[1:]:
                if m < last and inc: 
                    good = False
                    break
                elif inc == False and m > last:
                    good = False
                    break
                if not (abs(last-m) > 0 and abs(last-m) <= 3):
                    good = False
                    break
                last = m
            return good
        if check(l): 
            output += 1
        else: 
            for idx in range(len(l)):
                if check(l[:idx] + l[idx + 1:]):
                    output += 1
                    break
    return output

if __name__ == "__main__":
    input_path = utils.get_input_file(Path(__file__).resolve().parent / "data", 2)
    print(problem1(input_path))
    print(problem2(input_path))