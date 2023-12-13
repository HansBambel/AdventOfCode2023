from pathlib import Path


def check_reflection_get_leftover(pattern) -> int:
    my_stack = [pattern[0]]
    for i, line in enumerate(pattern[1:], start=1):
        if my_stack[-1] == line:
            # check if all previous elements are in reverse order in the rest of the pattern
            if all(pattern[j] == my_stack[-j - 1] for j in range(len(my_stack))) or all(
                p == my_stack[i - j - 1] for j, p in enumerate(pattern[i:])
            ):
                # we found a reflection
                return len(pattern) - len(my_stack)
        else:
            my_stack.append(line)
    return 0


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    patterns = data_file.split("\n\n")

    total = 0
    for pattern in patterns:
        # check horizontal reflection
        pattern = pattern.split("\n")
        leftover_horizontal = check_reflection_get_leftover(pattern)
        transposed = list(map(list, zip(*pattern)))
        transposed_pattern = ["".join(x) for x in transposed]
        # check vertical reflection
        leftover_vertical = check_reflection_get_leftover(transposed_pattern)
        total += leftover_horizontal + leftover_vertical * 100

    return total


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    patterns = data_file.split("\n\n")


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 405

    result = part_1("input.txt")
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == 1337

    result = part_2("input.txt")
    print(result)
