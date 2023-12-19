import re
from pathlib import Path

parsed = {}


def parse_instruction(instr: str) -> dict[str, tuple[callable, str]]:
    split_up = instr.split(",")
    instructions = {}
    for split in split_up:
        if ">" in split:
            part, condition = split.split(">")
            value, new_flow = condition.split(":")
            # see https://realpython.com/python-lambda/#evaluation-time
            instructions[part] = (lambda x, value=value: x > int(value), new_flow)
        elif "<" in split:
            part, condition = split.split("<")
            value, new_flow = condition.split(":")
            instructions[part] = (lambda x, value=value: x < int(value), new_flow)
        else:
            # set default of instruction
            # split in this case is the next flow
            instructions["default"] = (lambda: True, split)
    return instructions


def parse_workflows(workflows):
    parsed = {}
    for workflow in workflows.split("\n"):
        name, instr = workflow.split("{")
        instr = instr[:-1]
        parsed[name] = parse_instruction(instr)
    return parsed


def check_accepted(rating: dict[str, int], current_flow: str = "in") -> bool:
    if current_flow == "A":
        return True
    elif current_flow == "R":
        return False
    global parsed
    instruction = parsed[current_flow]
    for check_part, (comparison, new_flow) in instruction.items():
        if check_part == "default":
            return check_accepted(rating, new_flow)
        if comparison(rating[check_part]):
            return check_accepted(rating, new_flow)
    return check_accepted(rating, instruction["default"][1])


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    workflows, ratings = data_file.split("\n\n")
    global parsed
    parsed = parse_workflows(workflows)

    accepted = []
    for rating in ratings.split("\n"):
        rating_dict = {
            "x": int(re.findall(r"x=(\d+),", rating)[0]),
            "m": int(re.findall(r"m=(\d+),", rating)[0]),
            "a": int(re.findall(r"a=(\d+),", rating)[0]),
            "s": int(re.findall(r"s=(\d+)", rating)[0]),
        }
        if check_accepted(rating_dict):
            accepted.append(rating_dict)

    return sum(sum(rating.values()) for rating in accepted)


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n\n")


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 19114

    result = part_1("input.txt")
    assert result > 273933
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == 1337

    result = part_2("input.txt")
    print(result)
