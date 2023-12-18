from pathlib import Path
from queue import PriorityQueue


neighbors = [((-1, 0), "^"), ((+1, 0), "v"), ((0, -1), "<"), ((0, +1), ">")]

allowed_directions = {
    "^": ["<", ">", "^"],
    "v": ["<", ">", "v"],
    "<": ["^", "v", "<"],
    ">": ["^", "v", ">"],
    "": ["^", "v", "<", ">"],
}


def do_dijkstra(input_data: list[str]) -> int:
    # DIJKSTRA
    start_pos = (0, 0)
    goal_pos = (len(input_data) - 1, len(input_data[0]) - 1)

    distance_costs = {(start_pos, ""): 0}
    q = PriorityQueue()
    q.put((0, start_pos, ""))

    seen = {(start_pos, "")}
    prev: dict[tuple[int, int], tuple[int, int]] = {}
    while not q.empty():
        _, cur_pos, dirs = q.get()
        seen.add((cur_pos, dirs[-3:]))

        current_y, current_x = cur_pos

        new_neighbors = [
            ((current_y + n_y, current_x + n_x), dirs[-2:] + direction)  # add the direction
            for (n_y, n_x), direction in neighbors
            if (0 <= current_y + n_y < len(input_data))
            and (0 <= current_x + n_x < len(input_data[0]))
            and ((current_y + n_y, current_x + n_x), direction[-2:] + direction) not in seen
            and (dirs[-3:] != direction * 3)  # check if the direction would exceed 3 times in the same direction
            and (direction in allowed_directions[dirs[-1:]])
        ]
        for pos, new_dirs in new_neighbors:
            new_cost = distance_costs[(cur_pos, dirs)] + int(input_data[pos[0]][pos[1]])
            # end early
            if pos == goal_pos:
                return new_cost
            if new_cost < distance_costs.get((pos, new_dirs), 1e100):
                distance_costs[(pos, new_dirs)] = new_cost
                prev[pos] = cur_pos
                q.put((new_cost, pos, new_dirs))


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")

    return do_dijkstra(input_data)


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")

    return do_dijkstra(input_data)


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)

    result_ex = part_1("input_ex3.txt")
    print(result_ex)
    assert result_ex == 7

    result_ex = part_1("input_ex2.txt")
    print(result_ex)
    assert result_ex == 10

    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 102

    result = part_1("input.txt")
    assert result < 696
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == 94

    result = part_2("input_ex4.txt")
    print(result)
    assert result == 71

    result = part_2("input.txt")
    print(result)
