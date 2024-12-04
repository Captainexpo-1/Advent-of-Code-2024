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

    lines = [list(i) for i in utils.read_lines(input)]

    def find_word(grid, word):


        rows = len(grid)
        cols = len(grid[0])
        result = []

        # Define directions to search (horizontal, vertical, diagonal)
        directions = [(0, 1), (1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1), (-1, 0), (0, -1)]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == word[0]:
                    for dx, dy in directions:
                        r, c = row, col
                        match = True
                        for i in range(1, len(word)):
                            r += dx
                            c += dy
                            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != word[i]:
                                match = False
                                break
                        if match:
                            result.append(((row, col), (dx, dy)))

        return result
    # Add your solution logic here
    
    return len(find_word(lines, "XMAS"))

def problem2(input: str) -> int | str:
    output: int = 0
    lines = [list(i) for i in utils.read_lines(input)]
    out = [["." for _ in i] for i in lines]
    for idx, i in enumerate(lines):
        for jdx, j in enumerate(i):
            if j != "A": continue
            def find_mas(dir, i0,j0):
                m = []
                try: 
                    if i0 < 0 or j0 < 0: return False 
                    m.append(lines[i0][j0]=="M")
                except: return False
                try: 
                    if i0+dir[0] < 0 or j0+dir[1] < 0: return False 
                    m.append(lines[i0+dir[0]][j0+dir[1]]=="A")
                except: return False
                try:
                    if i0+dir[0]*2 < 0 or j0+dir[1]*2 < 0: return False 
                    m.append(lines[i0+dir[0]*2][j0+dir[1]*2]=="S")
                except: return False
                return all(m)
            if not find_mas((1,1), idx-1, jdx-1):
                if not find_mas((-1,-1), idx+1, jdx+1):
                    continue
            if not find_mas((1,-1), idx-1, jdx+1):
                if not find_mas((-1,1), idx+1, jdx-1):
                    continue
            out[idx][jdx] = "X"
            output += 1
    open("o.txt","w").write('\n'.join([''.join(i) for i in out]))
    return output


if __name__ == "__main__":
    input_path = utils.get_input_file(Path(__file__).resolve().parent / "data", 4)
    print(problem1(input_path))
    print(problem2(input_path))