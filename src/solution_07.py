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
    lines = utils.read_lines(input)

    def naive_solve(nums: list[int], target: int):
        positions = [None for _ in range(len(nums))]
        ops = ["+", "*"]
        
        def e():
            # combine operators like 1 + 2 + 3 + 4
            total = nums[0]
            for i in range(1, len(nums)):
                if positions[i-1] == "+":
                    total += nums[i]
                else:
                    total *= nums[i]
            return total

        # Generate all possible combinations of operators
        combos = list(itertools.product(ops, repeat=len(nums)-1))
        #print(combos)
        for combo in combos:
            for i in range(len(combo)):
                positions[i] = combo[i]
            if e() == target:
                return True
        return False

    for line in lines:
        s = line.split(":")
        num = int(s[0])
        others = [int(i) for i in s[1].split(" ")[1:]]
        if naive_solve(others, num):
            output += num

    return output

def problem2(input: str) -> int | str:
    output: int = 0
    lines = utils.read_lines(input)

    def naive_solve(nums: list[int], target: int):
        ops = ["+", "*", "||"]
        
        def e(positions):
            # combine operators like 1 + 2 + 3 + 4
            total = nums[0]
            i = 1
            while i < len(nums):
                if positions[i-1] == "+":
                    total += nums[i]
                elif positions[i-1] == "*":
                    total *= nums[i]
                else:
                    total = int(str(total) + str(nums[i]))
                i += 1
            return total

        # Generate all possible combinations of operators
        combos = list(itertools.product(ops, repeat=len(nums)-1))
        #print(combos)
        for combo in combos:
            if e(combo) == target:
                return True

        return False

    for idx, line in enumerate(lines):
        s = line.split(":")
        num = int(s[0])
        others = [int(i) for i in s[1].split(" ")[1:]]
        if naive_solve(others, num):
            output += num
        #print(f"{idx}/{len(lines)}")
        #print(f"Line {idx+1} of {len(lines)}: {output}",end="\r")
    return output


if __name__ == "__main__":
    input_path = utils.get_input_file(Path(__file__).resolve().parent / "data", 7)
    print(problem1(input_path))
    print(problem2(input_path))