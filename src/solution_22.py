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
    vals = [int(i) for i in utils.read_lines(input)]

    def get_next_num(num, n=0):
        if n == 2000:
            return num
        
        # num * 64 + mix + prune
        # num // 32 + mix + prune
        # num * 2048 + mix + prune
        
        mix_prune = lambda num, b: (num ^ b) % 16777216  
        num = mix_prune(num, num*64)
        num = mix_prune(num, num//32)
        num = mix_prune(num, num*2048)
        
        return get_next_num(num, n+1)
    
    return sum(get_next_num(i) for i in vals)

def problem2(input: str) -> int | str:
    output: int = 0
    vals = [int(i) for i in utils.read_lines(input)]

    def get_next_num(num):
        for i in range(2000):
            mix_prune = lambda num, b: (num ^ b) % 16777216  
            num = mix_prune(num, num*64)
            num = mix_prune(num, num//32)
            num = mix_prune(num, num*2048)
            yield num
    
    changes = {}
    
    prices = []
    changes = []
    for idx, i in enumerate(vals):
        print(idx,"/",len(vals), end='\r')
        prices.append([i]+[i%10 for i in get_next_num(i)])
    # get each set of 4 changes
    # e.g for prices = [1,3,4,9,2,3]
    # changes = [[2,1,5,-7],[1,5,-7,2],[5,-7,2,1]]
    for idx, p in enumerate(prices):
        g = set()
        c = []
        for i in range(1,len(p)-4):
            # append [(sequence, price at start of sequence, index of price)]
            m = [p[idx]-p[idx-1] for idx in range(i, i+4)]
            if str(m) not in g:
                c.append((m, p[i+3], idx))
                g.add(str(m))
        changes.append(c)
    print()
    #for c in changes:
        #print(list(filter(lambda x: x[0]==[-2,1,-1,3], c)))
    
    all_changes = utils.flatten(changes)
    
    possible_changes = collections.defaultdict(int)
    for (c, price, idx) in all_changes:
        possible_changes[str(c)] += price

    m = -1
    for k,v in possible_changes.items():
        if v > m:
            m = v
    
    return m

if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    input_path = utils.get_input_file(Path(__file__).resolve().parent / "data", 22)
    #print(problem1(input_path))
    print(problem2(input_path))