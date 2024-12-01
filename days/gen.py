import os

if __name__ == "__main__":
    template: str = open(os.path.join(os.path.dirname(__file__), "template.py"), "r").read()
    for i in range(1, 26):
        input_path: str = os.path.join(os.path.dirname(__file__), f"data/input_{i:02d}.txt")
        if not os.path.exists(input_path):
            # Create the empty file
            with open(input_path, "w") as f:
                pass
        solution_path: str = os.path.join(os.path.dirname(__file__), f"solution_{i:02d}.py")
        if not os.path.exists(solution_path):
            with open(solution_path, "w") as f:
                f.write(template)

