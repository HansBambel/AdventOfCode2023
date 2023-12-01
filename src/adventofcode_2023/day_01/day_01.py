import re
from pathlib import Path


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")
    total = 0
    for line in input_data:
        # remove chars and only keep digits
        line = "".join([char for char in line if char.isdigit()])
        # Only use the first and last digit
        line = line[0] + line[-1]
        total += int(line)
    return total


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")

    mapping = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    total = 0
    for line in input_data:
        # replace the first and last occurrence of the key with the value
        # find the match that has the smallest match
        regex = "(one|two|three|four|five|six|seven|eight|nine)"
        line_left = re.sub(re.compile(regex), lambda match: str(mapping[match.group(0)]), line, count=1)
        # now do the same reversed
        reversed_regex = regex[::-1]
        reversed_regex = "(" + reversed_regex[1:-1] + ")"
        line_right = re.sub(
            re.compile(reversed_regex), lambda match: str(mapping[match.group(0)[::-1]]), line[::-1], count=1
        )[::-1]

        # slap them together
        line = line_left + line_right
        # remove chars and only keep digits
        line = "".join([char for char in line if char.isdigit()])
        # Only use the first and last digit
        line = line[0] + line[-1]
        total += int(line)
    return total


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 142

    result = part_1("input.txt")
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result_ex = part_2("input_ex2.txt")
    print(result_ex)
    assert result_ex == 281

    result_ex = part_2("input_ex3.txt")
    print(result_ex)
    assert result_ex == 62

    # THIS IS AN IMPORTANT EXAMPLE: eighthree -> 83
    result_ex = part_2("input_ex4.txt")
    print(result_ex)
    assert result_ex == 83

    result = part_2("input.txt")
    # These were my previous submissions
    assert result < 54251, result
    assert result > 54235, result
    assert result > 54242, result
    assert result != 54245, result
    print(result)
