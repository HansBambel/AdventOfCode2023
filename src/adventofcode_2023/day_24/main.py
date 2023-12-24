from pathlib import Path
from sympy import Ray2D, Point
from tqdm import tqdm


def check_inside_area(point: Point, area_min: int, area_max: int):
    return (area_min <= point.x <= area_max) and (area_min <= point.y <= area_max)


def check_intersection(
    pos1: tuple[int, int, int], velo1: tuple[int, int, int], pos2: tuple[int, int, int], velo2: tuple[int, int, int]
):
    # check if they are intersecting (disregard Z) via math
    line1 = Ray2D(pos1[:2], (pos1[0] + velo1[0], pos1[1] + velo1[1]))
    line2 = Ray2D(pos2[:2], (pos2[0] + velo2[0], pos2[1] + velo2[1]))
    return line1.intersect(line2)


def part_1(input_file: str, area_min: int, area_max: int):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")
    hail = []
    for line in input_data:
        pos, velocity = line.split("@")
        pos_x, pos_y, pos_z = map(int, pos.split(","))
        velo_x, velo_y, velo_z = map(int, velocity.split(","))
        hail.append(((pos_x, pos_y, pos_z), (velo_x, velo_y, velo_z)))

    intersections_in_area = 0
    for i in tqdm(range(len(hail))):
        for j in range(i + 1, len(hail)):
            pos1, velo1 = hail[i]
            pos2, velo2 = hail[j]
            # check if they are intersecting and if so, check if it is inside the area
            are_intersecting = check_intersection(pos1, velo1, pos2, velo2)
            if are_intersecting:
                # check if it is inside the area
                if check_inside_area(are_intersecting.args[0], area_min, area_max):
                    intersections_in_area += 1

    return intersections_in_area


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt", 7, 27)
    print(result_ex)
    assert result_ex == 2

    result = part_1("input.txt", 200_000_000_000_000, 400_000_000_000_000)
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == 47

    result = part_2("input.txt")
    print(result)
