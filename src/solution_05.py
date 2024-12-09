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

def problem2(input: str) -> int:
    output: int = 0
    f = utils.read_file(input)
    (rules, updates) = f.split("\n\n")
    
    updates = [i for i in updates.split("\n")]
    updates = [[int(j) for j in i.split(",")] for i in updates]
    rules = [(int(i.split("|")[0]), int(i.split("|")[1])) for i in rules.split("\n")]
    r = {}

    for j in rules:
        r.setdefault(j[1], set())
        r[j[1]].add(j[0])  # r[key] = set(values), where key = num and values = set of nums that can before after key

    def is_valid_update(u):
        for idx, i in enumerate(u):
            for j in u[:idx]:
                if j not in r.get(i, []):
                    return False
        return True

    def fix_update(u):
        change = True
        update = u.copy()
        while change:
            change = False
            update = update.copy()
            # Make it so that the update is valid
            for idx, i in enumerate(update):
                for jdx, j in enumerate(update[:idx]):
                    if j not in r.get(i, []): # If j is not in the set of values that can come before i
                        update.insert(idx, update.pop(jdx))
                        print(update)
                        change = True
                        break
        return update

    for k in updates:
        if is_valid_update(k):
            continue
        fu = fix_update(k)
        print(fu)
        output += fu[len(fu)//2]
    return output

if __name__ == "__main__":
    input_path = utils.get_input_file(Path(__file__).resolve().parent / "data", 5)
    print(problem1(input_path))
    print(problem2(input_path))