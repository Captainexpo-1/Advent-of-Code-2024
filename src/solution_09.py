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

    k = []
    file = 0
    for i, val in enumerate(f):
        if i % 2 == 0:
            k.extend([file] * int(val))
            file += 1
        else:
            k.extend(["."] * int(val))

    empty_cache = [idx for idx, num in enumerate(k) if num == "."]

    for i in range(len(k) - 1, 0, -1):
        if k[i] != ".":
            idx = empty_cache.pop(0)
            k[idx], k[i] = k[i], k[idx]
        if all(x == "." for x in k[k.index("."):]):
            break

    output = sum(idx * num for idx, num in enumerate(k) if num != ".")
    return output
    
        

def problem2(input: str) -> int | str:
    output: int = 0
    f = utils.read_file(input)
    def print_output_visual(l):
        for i, (val, length) in enumerate(l):
            if val == None:
                print(f"{'.' * length}",end="")
            else:
                print(str(val)*length,end="")

    k = [] # list of ranges
    file = 0
    for i, val in enumerate(f):
        if i % 2 == 0:
            k.append((file, int(val)))
            file += 1
        else:
            k.append((None, int(val)))

    #print_output_visual(k)
    #print()
    def find_empties(l):
        return [(idx, num) for idx, num in enumerate(l) if num[0] == None]
    
    checked_maxes = set()
    
    def find_max_of_non_checked(l):
        return sorted([(num, idx) for idx, num in enumerate(l) if num not in checked_maxes and num[0]], key=lambda x: x[0], reverse=True)
    
    def combine_empty(l):
        new_l = []
        for i, (val, length) in enumerate(l):
            if val == None:
                if i > 0 and l[i-1][0] == None:
                    new_l[-1] = (None, new_l[-1][1] + length)
                else:
                    new_l.append((None, length))
            else:
                new_l.append((val, length))
        return new_l
    
    while len(ncm:=find_max_of_non_checked(k)) > 0:
        #print(len(ncm))
        max_val, max_idx = ncm[0]
        checked_maxes.add(max_val)
        empties = find_empties(k)
        # loop through the empties
        # if an empty is longer or equal than the max's length, fill it with the max
        # just fill it and leave the excess empty to the right of the max
        # if there are no empties that are longer or equal, leave the max alone
        for idx, (_, length) in empties:
            if max_idx < idx: continue
            if length == max_val[1]:
                k[idx] = max_val
                k[max_idx] = (None, max_val[1])
                break
            if length > max_val[1]:
                k[idx] = max_val
                k[max_idx] = (None, max_val[1])
                k.insert(idx + 1, (None, length - max_val[1]))

                break
        k = combine_empty(k)            
            #print_output_visual(k)
            #print()

    #print_output_visual(k)
    
    def calc_checksum_of_range(pos: int, r: tuple[int, int]) -> int:
        # checksum of a range is the sum of the range multiplied by the position of the element in the range
        # where the position is from {pos} to {pos + r[1]}
        if r[0] == None:
            return 0
        return sum((pos + i) * r[0] for i in range(r[1]))
    #print(k)
    
    i = 0
    for idx, val in enumerate(k):
        output += calc_checksum_of_range(i, val)
        i += val[1]
    return output
        

if __name__ == "__main__":
    input_path = utils.get_input_file(Path(__file__).resolve().parent / "data", 9)
    print(problem1(input_path))
    print(problem2(input_path))