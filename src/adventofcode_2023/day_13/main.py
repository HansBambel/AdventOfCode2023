from pathlib import Path


def check_reflection_get_leftover(pattern) -> int:
    for i, line in enumerate(pattern[1:], start=1):
        if pattern[i - 1] == line:
            # check if all previous elements are in reverse order in the rest of the pattern
            left = pattern[:i]
            right = pattern[i:]
            shorter, longer = (left, right) if len(left) < len(right) else (right, left)
            if set(shorter).issubset(set(longer)):
                # we found a reflection
                return i
    return 0


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    patterns = data_file.split("\n\n")

    total = 0
    for pattern in patterns:
        # check horizontal reflection
        pattern = pattern.split("\n")
        leftover_rows = check_reflection_get_leftover(pattern)
        leftover_cols = 0
        if leftover_rows == 0:
            transposed = list(map(list, zip(*pattern)))
            transposed_pattern = ["".join(x) for x in transposed]
            # check vertical reflection
            leftover_cols = check_reflection_get_leftover(transposed_pattern)
        total += leftover_rows * 100 + leftover_cols

    return total


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    patterns = data_file.split("\n\n")


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex1.txt")
    print(result_ex)
    assert result_ex == 5

    result_ex = part_1("input_ex2.txt")
    print(result_ex)
    assert result_ex == 400

    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 405

    result_ex = part_1("input_ex3.txt")
    print(result_ex)
    assert result_ex == 709

    result = part_1("input.txt")
    assert result < 38272
    assert result < 38261
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == 1337

    result = part_2("input_ex3.txt")
    print(result)
    assert result == 1400

    result = part_2("input.txt")
    print(result)
