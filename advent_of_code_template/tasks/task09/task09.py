from advent_of_code_template.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List
from itertools import combinations
import re


class Task09(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = 'The largest area is: %d'
        self.bonus_answer_text = 'The largest area completely inside the shape is: %d'
        self.task_number = 9

    def solve_task(self, input_file_content: List[str]):
        tiles = [[int(y) for y in x.strip().split(',')] for x in input_file_content]
        largest_area = 0
        for i, tile in enumerate(tiles):
            for j, other in enumerate(tiles[i + 1:]):
                x = abs(tile[0] - other[0]) + 1
                y = abs(tile[1] - other[1]) + 1
                area = x * y
                largest_area = max(largest_area, area)
        return largest_area

    def solve_bonus_task(self, input_file_content: List[str]):
        # note: this is not a general solution, there are some edge cases
        # (largest rectangle completely outside of shape) in which this does not work.
        red_tiles = [[int(y) for y in x.strip().split(',')] for x in input_file_content]
        edges = list(zip(red_tiles, red_tiles[1:] + [red_tiles[0]]))
        vertical_edges = [(x0, *sorted((y0, y1))) for (x0, y0), (x1, y1) in edges if x0 == x1]
        horizontal_edges = [(y0, *sorted((x0, x1))) for (x0, y0), (x1, y1) in edges if y0 == y1]

        largest_area = 0
        for (x0, y0), (x1, y1) in combinations(red_tiles, 2):
            min_x, min_y, max_x, max_y = min(x0, x1) + 0.5, min(y0, y1) + 0.5, max(x0, x1) - 0.5, max(y0, y1) - 0.5
            if not any(
                    (min_x <= v_x <= max_x and (min_v_y <= min_y <= max_v_y or min_v_y <= max_y <= max_v_y)) or
                    (min_y <= h_y <= max_y and (min_h_x <= min_x <= max_h_x or min_h_x <= max_x <= max_h_x))
                    for (v_x, min_v_y, max_v_y), (h_y, min_h_x, max_h_x)
                    in zip(vertical_edges, horizontal_edges)
            ):  # if no edge intersects with the borders of the rectangle
                largest_area = max(largest_area, (abs(x0 - x1) + 1) * (abs(y0 - y1) + 1))
        return largest_area

    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch("[0-9]+,[0-9]+\n?", line) for line in input_file_content)
