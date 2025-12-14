from functools import cache

from advent_of_code_template.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List
import re
from collections import deque


def find_number_of_paths(nodes_dict: dict[str, List[str]], start_node: str, end_node: str) -> int:
    current_nodes = deque([x for x in nodes_dict[start_node] if x != end_node])
    visited = [start_node]
    counter = 0 if end_node not in nodes_dict[start_node] else 1
    while len(current_nodes) > 0:
        current_node = current_nodes.popleft()
        visited.append(current_node)
        if current_node == 'out':
            continue
        children = nodes_dict[current_node]
        if end_node in children:
            counter += 1
        current_nodes.extend([x for x in children if x not in visited and x != end_node])
    return counter


class Task11(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = 'The number of paths from you to out is: %d'
        self.bonus_answer_text = 'The number of paths from svr over fft and dac to out is: %d'
        self.task_number = 11

    def solve_task(self, input_file_content: List[str]):
        nodes_dict = {y[0]: y[1:] for y in [[x[:3] for x in line.strip().split()] for line in input_file_content]}
        return find_number_of_paths(nodes_dict, 'you', 'out')

    def solve_bonus_task(self, input_file_content: List[str]):
        nodes_dict = {y[0]: y[1:] for y in [[x[:3] for x in line.strip().split()] for line in input_file_content]}

        @cache
        def path_count(start_node: str, end_node: str) -> int:
            if start_node == end_node:
                return 1
            elif start_node != 'out':
                return sum(path_count(next_node, end_node) for next_node in nodes_dict[start_node])
            else:
                return 0

        fft_to_dac = path_count('fft', 'dac')
        if fft_to_dac > 0:
            start_to_fft = path_count('svr', 'fft')
            dac_to_out = path_count('dac', 'out')
            return start_to_fft * fft_to_dac * dac_to_out
        else:
            start_to_dac = path_count('svr', 'dac')
            dac_to_fft = path_count('dac', 'fft')
            fft_to_out = path_count('fft', 'out')
            return start_to_dac * dac_to_fft * fft_to_out

    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch("[a-z]+:( [a-z]+)+\n?", line) for line in input_file_content)
