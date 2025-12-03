from advent_of_code_template.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List
import re


class Task03(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = '%d.'
        self.bonus_answer_text = '%d.'
        self.task_number = 3

    def max_joltage_for_n(self, number_list: str, n : int):
        numbers = [int(x) for x in number_list.strip()]
        max_list = []
        start_index = 0
        for i in range(n):
            cur_max = 0
            cur_idx = 0
            for j, num in enumerate(numbers[start_index:len(numbers) - n + i + 1]):
                if num > cur_max:
                    cur_max = num
                    cur_idx = j + start_index
            start_index = cur_idx + 1
            max_list.append(cur_max)
        return int("".join([str(x) for x in max_list]))


    def solve_task(self, input_file_content: List[str]):
        joltage_sum = 0
        for line in input_file_content:
            joltage_sum = joltage_sum + self.max_joltage_for_n(line, 2)
        return joltage_sum

    def solve_bonus_task(self, input_file_content: List[str]):
        joltage_sum = 0
        for line in input_file_content:
            joltage_sum = joltage_sum + self.max_joltage_for_n(line, 12)
        return joltage_sum

    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch("[0-9]+\n?", line) for line in input_file_content)
