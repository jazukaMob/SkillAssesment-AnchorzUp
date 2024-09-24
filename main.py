import itertools
import re


def validate_line(input_str):
    pattern = r'^\d+,\d+$'

    if not re.match(pattern, input_str):
        raise ValueError(f"Invalid line: {input_str}. Expected format is \"x,y\"")

    x, y = input_str.split(',')
    return int(x), int(y)


def generate_paths(x_, y_):
    steps = ['E'] * x_ + ['N'] * y_

    unique_paths = set(itertools.permutations(steps))

    paths_str = []
    pattern = r'(NNN(?!N))|(EEE(?!E))'

    for path in unique_paths:
        path_str = ''.join(path)
        if not re.search(pattern, path_str):
            paths_str.append(path_str)

    valid_paths = len(paths_str)
    print("Number of valid paths: {}".format(valid_paths))
    print("Routes for each valid path: " + ", ".join(paths_str) + "\n")
    return valid_paths


with open("input.txt", "r+") as f:
    lines = f.readlines()
    for line in lines:
        try:
            x, y = validate_line(line)
            generate_paths(x, y)
        except:
            print("skipping line...")
