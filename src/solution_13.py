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
import functools
import networkx
import sympy
from sympy.solvers.diophantine import diophantine
def problem1(input: str) -> int | str:
    output: int = 0
    vals = utils.read_file(input).split("\n\n")
    v: list[dict] = []
    
    for k in vals:
        m = k.split("\n")
        pp = m[2].replace("Prize: X=","").replace(" Y="," ").split(",")
        ba = m[0].replace("Button A: ","").replace("X+","").replace(" Y+"," ").split(",")
        bb = m[1].replace("Button B: ","").replace("X+","").replace(" Y+"," ").split(",")
        v.append({"a":(int(ba[0]),int(ba[1])),"b":(int(bb[0]),int(bb[1])),"p":(int(pp[0]),int(pp[1]))})
    
    for machine in v:
        ax, ay = machine["a"]
        bx, by = machine["b"]
        px, py = (machine["p"][0], machine["p"][1])
        

        b = (ax * py - ay * px) / (ax * by - ay * bx)
        a = (px - bx * b) / ax
        #print(a,b)
        if int(a) == a and int(b) == b:
            output += int(3 * a + b)
        # find an integer solution to a[0] * x + b[0] * y == p[0], a[1] * x + b[1] * y == p[1]
        # where we need to minimize 3*x + y

        # px = ax * a + bx * b
        # py = ay * a + by * b
        # a = (px - bx * b) / ax
        # a = (py - by * b) / ay
        # (px - bx * b) / ax = (py - by * b) / ay
        # ay * (px - bx * b) = ax * (py - by * b)
        # ay * px - ay * bx * b = ax * py - ax * by * b
        # ay * px - ax * py = ay * bx * b - ax * by * b
        # ay * px - ax * py = b * (ay * bx - ax * by)
        # b = (ay * px - ax * py) / (ay * bx - ax * by)
        # a = (px - bx * b) / ax

    return output
        
def problem2(input: str) -> int | str:
    output: int = 0
    vals = utils.read_file(input).split("\n\n")
    v: list[dict] = []
    
    for k in vals:
        m = k.split("\n")
        pp = m[2].replace("Prize: X=","").replace(" Y="," ").split(",")
        ba = m[0].replace("Button A: ","").replace("X+","").replace(" Y+"," ").split(",")
        bb = m[1].replace("Button B: ","").replace("X+","").replace(" Y+"," ").split(",")
        v.append({"a":(int(ba[0]),int(ba[1])),"b":(int(bb[0]),int(bb[1])),"p":(int(pp[0]),int(pp[1]))})
    
    for machine in v:
        ax, ay = machine["a"]
        bx, by = machine["b"]
        px, py = (machine["p"][0] + 10_000_000_000_000, machine["p"][1] + 10_000_000_000_000)
        print(ax,ay,bx,by,px,py)

        b = (ax * py - ay * px) / (ax * by - ay * bx)
        a = (px - bx * b) / ax
        #print(a,b)
        if int(a) == a and int(b) == b:
            output += int(3 * a + b)
        # find an integer solution to a[0] * x + b[0] * y == p[0], a[1] * x + b[1] * y == p[1]
        # where we need to minimize 3*x + y

        # px = ax * a + bx * b
        # py = ay * a + by * b
        # a = (px - bx * b) / ax
        # a = (py - by * b) / ay
        # (px - bx * b) / ax = (py - by * b) / ay
        # ay * (px - bx * b) = ax * (py - by * b)
        # ay * px - ay * bx * b = ax * py - ax * by * b
        # ay * px - ax * py = ay * bx * b - ax * by * b
        # ay * px - ax * py = b * (ay * bx - ax * by)
        # b = (ay * px - ax * py) / (ay * bx - ax * by)
        # a = (px - bx * (ay * px - ax * py) / (ay * bx - ax * by)) / ax

    return output

if __name__ == "__main__":
    input_path = utils.get_input_file(Path(__file__).resolve().parent / "data", 13)
    print(problem1(input_path))
    print(problem2(input_path))