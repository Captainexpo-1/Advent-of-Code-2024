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


def problem1(input: str) -> int | str:
    output: int = 0
    f = utils.read_file(input)
    reg, program = f.split("\n\n")
    reg = reg.split("\n")
    registers = {}
    for r in reg:
        m = r.split(": ")
        registers[m[0][-1]] = int(m[1])
    program = [int(i) for i in program.split(": ")[1].split(',')]
    
    
    IP = 0
    
    def get_lit(arg: int) -> int:
        return arg
    def get_combo(arg: int) -> int:
        combo = arg
        if combo <= 3:
            return arg
        else:
            match combo:
                case 4:
                    combo = registers["A"]
                case 5:
                    combo = registers["B"]
                case 6:
                    combo = registers["C"]   
        return combo
    out = []
    while IP < len(program):
        opcode = program[IP]
        arg = program[IP+1]

        match opcode:
            case 0: # adv
                registers["A"] = int(registers["A"] / (2**get_combo(arg)))
            case 1: # bxl
                registers ["B"] = registers["B"] ^ get_lit(arg)
            case 2: # bst
                registers["B"] = get_combo(arg) % 8
            case 3: # jnz
                if registers["A"] != 0:
                    IP = get_lit(arg)
                    continue
            case 4: # bxc
                registers["B"] = registers["B"] ^ registers["C"]
            case 5: # out
                out += [get_combo(arg) % 8]
            case 6: # bdv
                registers["B"] = registers["A"] // (2**get_combo(arg))
            case 7: # cdv
                registers["C"] = registers["A"] // (2**get_combo(arg))
        #print(registers, IP, opcode, arg)
        IP += 2
    
    return ','.join([str(i) for i in out])

def run_program(registers: dict, program: list) -> list:
    IP = 0
    
    def get_lit(arg: int) -> int:
        return arg
    
    def get_combo(arg: int) -> int:
        combo = arg
        if combo <= 3:
            return arg
        else:
            match combo:
                case 4:
                    combo = registers["A"]
                case 5:
                    combo = registers["B"]
                case 6:
                    combo = registers["C"]   
        return combo
    
    out = []
    while IP < len(program):
        opcode = program[IP]
        arg = program[IP+1]

        match opcode:
            case 0: # adv
                registers["A"] = int(registers["A"] / (2**get_combo(arg)))
            case 1: # bxl
                registers["B"] = registers["B"] ^ get_lit(arg)
            case 2: # bst
                registers["B"] = get_combo(arg) % 8
            case 3: # jnz
                if registers["A"] != 0:
                    IP = get_lit(arg)
                    continue
            case 4: # bxc
                registers["B"] = registers["B"] ^ registers["C"]
            case 5: # out
                out += [get_combo(arg) % 8]
            case 6: # bdv
                registers["B"] = registers["A"] // (2**get_combo(arg))
            case 7: # cdv
                registers["C"] = registers["A"] // (2**get_combo(arg))
        IP += 2
    
    return out

def problem2(input: str) -> int | str:
    f = utils.read_file(input)
    reg, program = f.split("\n\n")
    reg = reg.split("\n")
    registers = {}
    for r in reg:
        m = r.split(": ")
        registers[m[0][-1]] = int(m[1])

    program = [int(i) for i in program.split(": ")[1].split(',')]

    for A in itertools.count(202972175280680-1000, step=1): # the final search started at 202972175280680-1000

        registers["A"] = A
        out = run_program(registers, program)
        
        if out == program:
            return f"RESULT: {A} {out} {program}"
        
        # I just kept narrowing down the search space using these fricking and statements
        # If I found a place that fulfilled all the previous 'and' statements
        # I would narrow the search space, lower the step size, and add another and statement
        # This continued until I found the answer when the step size was 1
        if out[-1] ==   program[-1] \
        and out[-2] ==  program[-2] \
        and out[-3] ==  program[-3] \
        and out[-4] ==  program[-4] \
        and out[-5] ==  program[-5] \
        and out[-6] ==  program[-6] \
        and out[-7] ==  program[-7] \
        and out[-8] ==  program[-8] \
        and out[-9] ==  program[-9] \
        and out[-10] == program[-10] \
        and out[-11] == program[-11] \
        and out[-12] == program[-12] \
        and out[-13] == program[-13] \
        and out[-14] == program[-14] \
        and out[-15] == program[-15]:
            print(A, len(out), out)    
        
def test_automation(input: str, do_log=False) -> int | str:
    f = utils.read_file(input)
    reg, program = f.split("\n\n")
    reg = reg.split("\n")
    registers = {}
    for r in reg:
        m = r.split(": ")
        registers[m[0][-1]] = int(m[1])

    program = [int(i) for i in program.split(": ")[1].split(',')]

    def cmp_lists(l1, l2):
        k = 0
        # compare backwards
        for i in range(len(l1)):
            if l1[-(i+1)] == l2[-(i+1)]:
                k += 1
            else:
                return k
        return k

    start_search = 0
    step_size = 100_000_000_000
    last_best_comp = 0
    while True:
        if do_log: print(start_search, step_size, last_best_comp)
        for A in itertools.count(start_search, step=step_size):
            registers["A"] = A
            out = run_program(registers, program)
            if len(out) < len(program):
                start_search += step_size*10
                break
            if out == program:
                return f"RESULT: {A} {out} {program}"
            
            if cmp_lists(out, program) > last_best_comp:
                last_best_comp = cmp_lists(out, program)
                start_search = A - step_size
                step_size = step_size // 10
                break
        


if __name__ == "__main__":
    input_path = utils.get_input_file(Path(__file__).resolve().parent / "data", 17)
    print(problem1(input_path))
    print(problem2(input_path))
    print(test_automation(input_path, do_log=True))