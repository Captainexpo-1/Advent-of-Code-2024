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
import sympy
import time


def problem1(input: str) -> int | str:
    output: int = 1
    f = utils.read_lines(input)
    m = []
    for i in f:
        l,n = i.split(" ")
        lala = l.replace("p=","").split(",")
        nana = n.replace("v=","").split(",")
        m.append(((int(lala[0]),int(lala[1])),(int(nana[0]),int(nana[1]))))
    w,t = 101, 103
    def sim_robot(robot: tuple[tuple[int, int], tuple[int, int]]):
        (x,y),(vx,vy) = robot
        for i in range(100):
            x += vx
            y += vy
            # make them loop around
            x = x % w
            y = y % t
        return (x,y)
    
    def sim_robots(robots: list[tuple[tuple[int, int], tuple[int, int]]]):
        r = []
        for robot in robots:
            k = sim_robot(robot)
            r.append(k)
        return r
    robots = sim_robots(m)
    
    def get_quadrant(pos: tuple[int, int]):

        x,y = pos
        if x == w // 2 or y == t // 2:
            return None
        if x < w // 2:
            if y < t // 2:
                return 1
            else:
                return 3
        else:
            if y < t // 2:
                return 2
            else:
                return 4
    print(robots)
    quadrants = {1:0,2:0,3:0,4:0}
    for r in robots:
        q = get_quadrant(r)
        if q: quadrants[q] += 1
    
    
    print(quadrants)
    for q in quadrants.values():
        output *= q
            
    
    return output

def problem2(input: str) -> int | str:
    output: int = 1
    f = utils.read_lines(input)
    m = []
    for i in f:
        l,n = i.split(" ")
        lala = l.replace("p=","").split(",")
        nana = n.replace("v=","").split(",")
        m.append(((int(lala[0]),int(lala[1])),(int(nana[0]),int(nana[1]))))
    w,t = 101, 103
    

    def sim_robot(robot: tuple[tuple[int, int], tuple[int, int]], i):
        (x,y),(vx,vy) = robot
        x += vx * i
        y += vy * i
        # make them loop around
        x = x % w
        y = y % t
        return (x,y)
    
    def sim_robots(robots: list[tuple[tuple[int, int], tuple[int, int]]]):
        i = 0

        while True:
            print(i)
            grid = [[0 for _ in range(w)] for j in range(t)]
            for robot in robots:
                k = sim_robot(robot, i)
                
                grid[k[1]][k[0]] += 1 
            
            n = True 
            for p in grid:
                for q in p:
                    if q > 1:
                        n = False
                        break
            if n:
                return i
            
            i += 1
    
    return sim_robots(m)

if __name__ == "__main__":
    input_path = utils.get_input_file(Path(__file__).resolve().parent / "data", 14)
    print(problem1(input_path))
    print(problem2(input_path))