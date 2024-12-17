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
import time
import networkx
import numpy as np
from heapq import heappush, heappop


def problem1(input: str) -> int | str:
    f = utils.read_grid(input)
    s_pos = None
    e_pos = None
    height = len(f)
    width = len(f[0])

    for idx in range(height):
        for jdx in range(width):
            if f[idx][jdx] == "S":
                f[idx][jdx] = "."
                s_pos = complex(jdx, idx)
            elif f[idx][jdx] == "E":
                f[idx][jdx] = "."
                e_pos = complex(jdx, idx)

    print(s_pos, e_pos)
    
    start_direction = 1
    heap = []
    heappush(heap, (0, (s_pos.real, s_pos.imag), (start_direction.real, start_direction.imag))) 

    visited = {}

    visited[(s_pos, start_direction)] = (0, None, None)

    while heap:
        cost, (p0, p1), (d0, d1) = heappop(heap)
        pos = complex(p0, p1)
        direction = complex(d0, d1)
        if pos == e_pos:
            break

        if visited[(pos, direction)][0] < cost:
            continue

        y = int(pos.imag)
        x = int(pos.real)
        if not (0 <= y < height and 0 <= x < width):
            continue
        if f[y][x] == "#":
            continue

        for turn_factor in [1, 1j, -1j]:
            new_dir = direction * turn_factor
            new_pos = pos + new_dir
            move_cost = 1 if turn_factor == 1 else 1001
            new_cost = cost + move_cost

            state = (new_pos, new_dir)
            if state not in visited or visited[state][0] > new_cost:
                visited[state] = (new_cost, pos, direction)
                heappush(heap, (new_cost, (new_pos.real, new_pos.imag), (new_dir.real, new_dir.imag)))
                
    best_state = None
    best_cost = math.inf
    for (p, d), (c, par_p, par_d) in visited.items():
        if p == e_pos and c < best_cost:
            best_cost = c

    return best_cost

def reconstruct_paths(end_state, visited, start_state):
    if end_state == start_state:
        return [[end_state[0]]]

    all_paths = []
    cost, parents = visited[end_state]
    for p in parents:
        sub_paths = reconstruct_paths(p, visited, start_state)
        for sp in sub_paths:
            all_paths.append(sp + [end_state[0]])
    return all_paths

def problem2(input: str) -> int | str:
    f = utils.read_grid(input)
    s_pos = None
    e_pos = None
    height = len(f)
    width = len(f[0])

    for idx in range(height):
        for jdx in range(width):
            if f[idx][jdx] == "S":
                f[idx][jdx] = "."
                s_pos = complex(jdx, idx)
            elif f[idx][jdx] == "E":
                f[idx][jdx] = "."
                e_pos = complex(jdx, idx)
    start_direction = 1
    start_state = (s_pos, start_direction)

    heap = []
    heappush(heap, (0, (s_pos.real, s_pos.imag), (start_direction.real, start_direction.imag)))

    visited = {start_state: (0, [])}

    best_cost = math.inf
    end_states = []

    while heap:
        cost, (px, py), (dx, dy) = heappop(heap)
        pos = complex(px, py)
        direction = complex(dx, dy)
        state = (pos, direction)

        current_cost, _ = visited.get(state, (math.inf, []))
        if current_cost < cost:
            continue

        if pos == e_pos:
            if cost < best_cost:
                best_cost = cost
                end_states = [state]
            elif cost == best_cost:
                end_states.append(state)
            continue

        y = int(pos.imag)
        x = int(pos.real)
        if not (0 <= y < height and 0 <= x < width):
            continue
        if f[y][x] == "#":
            continue

        for turn_factor in [1, 1j, -1j]:
            new_dir = direction * turn_factor
            new_pos = pos + new_dir
            move_cost = 1 if turn_factor == 1 else 1001
            new_cost = cost + move_cost

            new_state = (new_pos, new_dir)
            old_cost, old_parents = visited.get(new_state, (math.inf, []))

            if new_cost < old_cost:
                visited[new_state] = (new_cost, [state])
                heappush(heap, (new_cost, (new_pos.real, new_pos.imag), (new_dir.real, new_dir.imag)))
            elif new_cost == old_cost:
                visited[new_state][1].append(state)

    all_best_paths = []
    for end_state in end_states:
        all_best_paths.extend(reconstruct_paths(end_state, visited, start_state))

    a = []
    for i in all_best_paths:
        a.extend(i)
    

    return len(set(a))

if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    input_path = utils.get_input_file(Path(__file__).resolve().parent / "data", 16)
    #print(problem1(input_path))
    print(problem2(input_path))