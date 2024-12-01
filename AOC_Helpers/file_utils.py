import ast

def get_input_file(data_path: str, day: int) -> str:
    """
    Get the path to the input file for the given problem.

    :param data_path: Path to the data directory.
    :param problem: Problem number.
    :return: Path to the input file.
    """
    return f"{data_path}/input_{day:02d}.txt"

def list_from_file(file_path):
    """
    Read the file containing the brick data and parse it into a Python list.

    :param file_path: Path to the file containing the brick data.
    :return: Parsed list of bricks.
    """
    with open(file_path, 'r') as file:
        data = file.read()
        ls = ast.literal_eval(data)
    return ls