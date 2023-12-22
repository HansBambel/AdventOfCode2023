from pathlib import Path
from skspatial.objects import LineSegment


def brick_can_fall(brick: LineSegment, lower_bricks: list[LineSegment]) -> bool:
    if brick.point_a[2] <= 1 or brick.point_b[2] <= 1:
        return False
    moved_brick = LineSegment(
        [brick.point_a[0], brick.point_a[1], brick.point_a[2] - 1],
        [brick.point_b[0], brick.point_b[1], brick.point_b[2] - 1],
    )
    for lower_brick in lower_bricks:
        try:
            moved_brick.intersect_line_segment(lower_brick)
            return False
        except ValueError:
            continue
    return True


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")

    bricks = []
    for brick_raw in input_data:
        start, end = brick_raw.split("~")
        start_x, start_y, start_z = map(int, start.split(","))
        end_x, end_y, end_z = map(int, end.split(","))
        bricks.append(LineSegment([start_x, start_y, start_z], [end_x, end_y, end_z]))

    # Move the bricks down until they JUST don't intersect
    # sort the bricks first by z
    bricks.sort(key=lambda brick: max(brick.point_a[2], brick.point_b[2]))

    for i, brick in enumerate(bricks):
        lower_bricks = bricks[:i]
        while brick_can_fall(brick, lower_bricks):
            brick.point_a[2] -= 1
            brick.point_b[2] -= 1

    # Count the number of bricks that can safely be disintegrated
    deletable_bricks = []
    for i, brick in enumerate(bricks):
        lower_bricks = bricks[:i]
        upper_bricks = bricks[i + 1 :]
        deletable = True
        for j, upper_brick in enumerate(upper_bricks):
            if brick_can_fall(upper_brick, lower_bricks + upper_bricks[:j] + upper_bricks[j + 1 :]):
                deletable = False
                break
        if deletable:
            deletable_bricks.append(brick)
    return len(deletable_bricks)


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 5

    result = part_1("input.txt")
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == 1337

    result = part_2("input.txt")
    print(result)
