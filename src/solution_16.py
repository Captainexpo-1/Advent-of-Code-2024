import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import AOC_Helpers as utils
import re, os, itertools, collections, math

def problem1(input: str) -> int|str:
    output: int = 0
    lines = utils.read_lines(input)
    
    return output

def problem2(input: str) -> int|str:
    output: int = 0
    lines = utils.read_lines(input)
    
    return output

if __name__ == "__main__":
    input_path = utils.get_input_file(os.path.dirname(__file__), 16)
    print(problem1(input_path))
    print(problem2(input_path))