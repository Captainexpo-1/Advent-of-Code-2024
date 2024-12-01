import os
import _template
if __name__ == "__main__":
    template = _template.template
    for day in range(1, 26):
        input_path: str = os.path.join(os.path.dirname(__file__), f"data/input_{day:02d}.txt")
        if not os.path.exists(input_path):
            # Create the empty file
            with open(input_path, "w") as f:
                pass
        solution_path: str = os.path.join(os.path.dirname(__file__), f"solution_{day:02d}.py")
        if not os.path.exists(solution_path):
            with open(solution_path, "w") as f:
                f.write(template(day))

