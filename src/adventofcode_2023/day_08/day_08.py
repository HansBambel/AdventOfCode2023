import math
import re
from pathlib import Path


def _parse_mappings(original) -> dict[str, tuple[str, str]]:
    mapping = {}
    for line in original.split("\n"):
        key, lr = line.split(" = ")
        mapping[key] = re.findall(r"\w+", lr)
    return mapping


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    instructions, mappings = data_file.split("\n\n")
    mappings = _parse_mappings(mappings)

    current = "AAA"
    steps = 0
    while current != "ZZZ":
        next_instr = instructions[steps % len(instructions)] == "R"
        current = mappings[current][next_instr]
        steps += 1
    return steps


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    instructions, mappings = data_file.split("\n\n")
    mappings = _parse_mappings(mappings)

    current_nodes = [node for node in mappings.keys() if node[-1] == "A"]
    steps = 0
    found_loop_after = []
    while len(current_nodes) > 0:
        next_instr = instructions[steps % len(instructions)] == "R"
        for i, current in enumerate(current_nodes):
            current_nodes[i] = mappings[current][next_instr]
        steps += 1
        for current in current_nodes:
            if current[-1] == "Z":
                found_loop_after.append(steps)
        current_nodes = [node for node in current_nodes if node[-1] != "Z"]

    # math.prod(found_loop_after)
    # this result is one "save" step where they all end on Z, but we want to find the first time this happened
    # --> the least common multiplier
    return math.lcm(*found_loop_after)


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 2

    result_ex = part_1("input_ex2.txt")
    print(result_ex)
    assert result_ex == 6

    result = part_1("input.txt")
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex3.txt")
    print(result)
    assert result == 6

    result = part_2("input.txt")
    assert result < 12410494419143079334048741
    assert result == 8811050362409
    print(result)
