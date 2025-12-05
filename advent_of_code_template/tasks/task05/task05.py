from advent_of_code_template.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List
import re
from collections import deque


def parse_input(input_list: List[str]) -> (List[List[int]], List[int]):
    ranges = []
    ids = []
    for line in input_list:
        if re.fullmatch("[0-9]+-[0-9]+\n?", line):
            ranges.append([int(x) for x in line.strip().split('-')])
        if re.fullmatch("[0-9]+\n?", line):
            ids.append(int(line.strip()))
    return ranges, ids


class Task05(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = 'The amount of provided ids that are fresh is: %d'
        self.bonus_answer_text = 'All ranges combined, the number of fresh ids is: %d'
        self.task_number = 5

    def solve_task(self, input_file_content: List[str]):
        ranges, ids = parse_input(input_file_content)
        fresh_counter = 0
        for ingredient_id in ids:
            for fresh_range in ranges:
                if fresh_range[0] <= ingredient_id <= fresh_range[1]:
                    fresh_counter = fresh_counter + 1
                    break
        return fresh_counter

    def solve_bonus_task(self, input_file_content: List[str]):
        ranges, ids = parse_input(input_file_content)
        sorted_ranges = sorted(ranges, key=lambda x: x[0])
        merged_ranges = []
        done = False
        while not done:
            done = True
            cont = False
            for i, fresh_range in enumerate(sorted_ranges):
                if cont:
                    cont = False
                    continue
                if i + 1 < len(sorted_ranges) and sorted_ranges[i][1] >= sorted_ranges[i+1][0]:
                    merged_ranges.append([sorted_ranges[i][0], max(sorted_ranges[i][1], sorted_ranges[i+1][1])])
                    cont = True
                    done = False
                else:
                    merged_ranges.append(sorted_ranges[i])
            sorted_ranges = merged_ranges
            merged_ranges = []

        id_count = 0
        for fresh_range in sorted_ranges:
            id_count = id_count + fresh_range[1] - fresh_range[0] + 1

        return id_count

    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch("[0-9]+-[0-9]+\n?", line) or re.fullmatch("\n*", line) or
                   re.fullmatch("[0-9]+\n?", line) for line in input_file_content)
