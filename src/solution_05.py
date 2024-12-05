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
    (rules, updates) = f.split("\n\n")
    #lines = [(int(i.split("|")[0]),int(i.split("|")[1]))for i in ]
    
    updates = [i for i in updates.split("\n")]
    updates = [[int(j) for j in i.split(",")] for i in updates]
    rules = [(int(i.split("|")[0]),int(i.split("|")[1])) for i in rules.split("\n")]
    r = {}

    for j in rules:
        r.setdefault(j[1], set())
        r[j[1]].add(j[0])

    for update in updates:
        print(update)
        good = True
        for idx, num in enumerate(update):
            win = update[:idx]
            for w in win:
                if w not in r[num]:
                    good = False
                    break
            if not good:
                break
        if good:
            output += update[len(update)//2]
                    

    return output

def problem2(input: str) -> int | str:
    output: int = 0
    f = utils.read_file(input)
    (rules, updates) = f.split("\n\n")
    #lines = [(int(i.split("|")[0]),int(i.split("|")[1]))for i in ]
    
    updates = [i for i in updates.split("\n")]
    updates = [[int(j) for j in i.split(",")] for i in updates]
    rules = [(int(i.split("|")[0]),int(i.split("|")[1])) for i in rules.split("\n")]
    r = {}

    for j in rules:
        r.setdefault(j[1], set())
        r[j[1]].add(j[0])

    for k in updates:
        #print(update)
        update = k.copy()
        good = True
        idx = 0
        while idx < len(update):
            num = k[idx]
            #print("N",update,k)
            for jdx in range(idx):
                if update[jdx] not in r.get(num, set()):
                    # Bad number
                    good = False
                    print("Before change", idx, jdx, update, num, update[jdx], r.get(num, set()))
                    n = update.pop(jdx)
                    update.insert(idx + 1, n)
                    print("After change", update)
            idx += 1

        if not good:
            #print("BAD: ",end=" ")
            #print(update)
            output += update[len(update)//2]
        #print(update)
    return output

if __name__ == "__main__":
    input_path = utils.get_input_file(Path(__file__).resolve().parent / "data", 5)
   # print(problem1(input_path))
    print(problem2(input_path))