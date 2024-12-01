import sys
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import AOC_Helpers as utils
import re
import itertools
import collections
import math

def problem1(input: str) -> int | str:
    output: int = 0
    lines = utils.read_lines(input)
    # Add your solution logic here
    
    return output

def problem2(input: str) -> int | str:
    output: int = 0
    lines = utils.read_lines(input)
    # Add your solution logic here
    
    return output

if __name__ == "__main__":
    input_path = utils.get_input_file(Path(__file__).resolve().parent / "data", 20)
    print(problem1(input_path))
    print(problem2(input_path))