import math
import re

PRINT_STEPS = False


def validate_line(input_str):
    pattern = r'^\d+,\d+$'

    if not re.match(pattern, input_str):
        raise ValueError(f"Invalid line: {input_str}. Expected format is \"x,y\"")

    x, y = input_str.split(',')
    return int(x), int(y)


def generate_sequences_recursive(x_, y_, path='', sequences=None):
    if sequences is None:
        sequences = []
    if x_ == 0 and y_ == 0:
        sequences.append(path)
    if x_ > 0:
        generate_sequences_recursive(x_ - 1, y_, path + 'E', sequences)
    if y_ > 0:
        generate_sequences_recursive(x_, y_ - 1, path + 'N', sequences)
    return sequences


def generate_paths(x_, y_):
    print(f"Input: {x_, y_}")
    valid_paths = math.factorial(x + y) // (math.factorial(x) * math.factorial(y))
    print("Number of valid paths: {}".format(valid_paths))

    if PRINT_STEPS:
        unique_paths = generate_sequences_recursive(x_, y_)
        exclude_pattern = r"(?<!N)N{3}(?!N)|(?<!E)E{3}(?!E)"

        paths_str = []

        for path in unique_paths:
            if re.search(exclude_pattern, path):
                valid_paths -= 1
                continue
            paths_str.append(path)

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
