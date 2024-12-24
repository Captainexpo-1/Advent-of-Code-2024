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
import matplotlib.pyplot as plt
from enum import Enum
    



def problem1(input: str) -> int | str:
    output: int = 0
    
    wires = {}
    
    f = utils.read_file(input)
    l1, l2 = f.split("\n\n")
    
    connections = {}
    def add_default(wire):
        nonlocal wires
        if wire not in wires:
            wires[wire] = None
    for line in utils.lines(l1):
        l = line.split(": ")
        wires[l[0]] = int(l[1])
    
    for line in utils.lines(l2):
        l0, l1 = line.split(" -> ")
        k = l0.split(" ")
        add_default(k[0])
        add_default(k[-1])
        add_default(l1)
        if (k[0], k[2]) in connections:
            connections[(k[0],k[2])].append([k[1], l1])
            continue
        # connections[a][b] = [op, c]
        connections[(k[0],k[2])] = [[k[1], l1]]

    #print(connections)
    
    def all_zs_filled():
        for k,v in wires.items():
            if k[0] == "z" and v is None:
                return False
        zs = sorted(filter(lambda x: x[0] == "z", wires.keys()), reverse=True)
        #print(zs)
        return ''.join([str(wires[z]) for z in zs])

    while (m:=all_zs_filled()) is False and len(connections.keys()) > 0:
        #print(len(connections.keys()))
        for k in list(connections.keys()):
            vs = connections[k]
            for v in vs:
                wire1, wire2 = k
                op, out = v
                
                if wires[wire1] is None or wires[wire2] is None:
                    continue
                
                match op:
                    case "AND":
                        wires[out] = wires[wire1] & wires[wire2]    
                    case "OR":
                        wires[out] = wires[wire1] | wires[wire2]
                    case "XOR":
                        wires[out] = wires[wire1] ^ wires[wire2]
                #print(f"{wire1} {op} {wire2} -> {out} = {wires[out]}")
                connections[(wire1, wire2)].remove(v)
                if len(connections[(wire1, wire2)]) == 0:
                    del connections[(wire1, wire2)]
    
    if m == False:
        zs = sorted(filter(lambda x: x[0] == "z", wires.keys()), reverse=True)
        #print(zs)
        m= ''.join([str(wires[z]) for z in zs])
            
    return int(m,2)


def problem2(input: str) -> int | str:
    wires = {}
    
    f = utils.read_file(input)
    l1, l2 = f.split("\n\n")
    
    connections = {}
    def add_default(wire):
        nonlocal wires
        if wire not in wires:
            wires[wire] = None
    for line in utils.lines(l1):
        l = line.split(": ")
        wires[l[0]] = int(l[1])
    
    for line in utils.lines(l2):
        l0, l1 = line.split(" -> ")
        k = l0.split(" ")
        add_default(k[0])
        add_default(k[-1])
        add_default(l1)
        if tuple(sorted([k[0],k[2]])) in connections:
            connections[tuple(sorted([k[0],k[2]]))].append([k[1], l1])
            continue
        # connections[a][b] = [op, c]
        connections[tuple(sorted([k[0],k[2]]))] = [[k[1], l1]]

    #print(connections)
    def get_num(prefix):
        zs = sorted(filter(lambda x: x[0] == prefix, wires.keys()), reverse=True)
        return int(''.join([str(wires[z]) for z in zs]),2)
    
    desired = get_num("x")+get_num("y")    
    
    def get_all_of_wire(wire):
        c=[]
        for k,v in connections.items():
            if wire in k:
                w = 
                c.append([k,v]) 
        return c
    def get_full_adder(a, b):
        adder = {
            "a": a,
            "b": b,
            "cin": None,
            "a ^ b": None,
            "a & b": None,
            "sum": None,
            "cin & (a ^ b)": None,
            "cout": None,
        }
        ab = connections.get((a,b),[])
        ab = sorted(ab)
        
        adder["a ^ b"] = ab[1][1]
        adder["a & b"] = ab[0][1]
        k = get_all_of_wire(adder["a ^ b"])
        adder["cin"] = k[0] if k else None
        if adder["cin"] == None:
            return adder
        
        adder["cin & (a ^ b)"] = connections[adder["cin"]]
        return adder
    
    for k,v in connections.items():
        if set([k[0][0], k[1][0]]) == set(["x","y"]):
            
            print(get_full_adder(*k))
    
    return desired


if __name__ == "__main__":
    input_path = utils.get_input_file(Path(__file__).resolve().parent / "data", 24)
    print(problem1(input_path))
    print(problem2(input_path))