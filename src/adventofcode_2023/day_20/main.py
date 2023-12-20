from collections import defaultdict
from pathlib import Path

from tqdm import tqdm

instructions = {}


def push_button(conj_nodes, flipped_on, flipped_off) -> tuple[int, int]:
    global instructions
    low_pulse, high_pulse = 1, 0
    Q = [("broadcaster", False, "Button")]
    while Q:
        part, is_high_pulse, from_node = Q.pop(0)
        next_nodes = instructions.get(part, [])

        if (part in flipped_on or part in flipped_off) and not is_high_pulse:
            if part in flipped_on:
                # send low pulse to all next nodes
                Q.extend((next_node, False, part) for next_node in next_nodes)
                low_pulse += len(next_nodes)
                flipped_on.remove(part)
                flipped_off.add(part)
            else:
                # send high pulse to all next nodes
                Q.extend((next_node, True, part) for next_node in next_nodes)
                high_pulse += len(next_nodes)
                flipped_off.remove(part)
                flipped_on.add(part)
        elif part in conj_nodes:
            conj_nodes[part][from_node] = is_high_pulse
            if all(conj_nodes[part].values()):
                # send low pulse to all next nodes
                Q.extend((next_node, False, part) for next_node in next_nodes)
                low_pulse += len(next_nodes)
            else:
                # send high pulse to all next nodes
                Q.extend((next_node, True, part) for next_node in next_nodes)
                high_pulse += len(next_nodes)
        elif part == "broadcaster":
            Q.extend((next_node, is_high_pulse, part) for next_node in next_nodes)
            if is_high_pulse:
                high_pulse += len(next_nodes)
            else:
                low_pulse += len(next_nodes)

    return low_pulse, high_pulse


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")
    low = 0
    high = 0
    global instructions
    instructions = {}
    flipped_on = set()
    flipped_off = set()
    conj_nodes = defaultdict(dict)
    for line in input_data:
        left, right = line.split(" -> ")
        next_list = right.split(", ")
        if left == "broadcaster":
            instructions[left] = next_list
        else:
            if left[0] == "&":
                instructions[left[1:]] = next_list
                conj_nodes[left[1:]] = {}
            else:
                instructions[left[1:]] = next_list
                flipped_off.add(left[1:])
    # initialize all conjunction nodes inputs to zero
    for node, inputs in conj_nodes.items():
        for parent, next_list in instructions.items():
            if node in next_list:
                inputs[parent] = False

    for _ in tqdm(range(1000)):
        new_low, new_high = push_button(conj_nodes, flipped_on, flipped_off)
        low += new_low
        high += new_high
    return low * high


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 32000000

    result_ex = part_1("input_ex2.txt")
    print(result_ex)
    assert result_ex == 11687500

    result = part_1("input.txt")
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == 1337

    result = part_2("input.txt")
    print(result)
