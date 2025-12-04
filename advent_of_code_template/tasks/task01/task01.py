from advent_of_code_template.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List
import re


class Task01(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = 'The number of times the dial stops at zero is: %d'
        self.bonus_answer_text = 'The number of times, 0 is passed by the dial is: %d'
        self.task_number = 1

    def solve_task(self, input_file_content: List[str]):
        current_position = 50
        zero_counter = 0
        for line in input_file_content:
            number = int(line[1:])
            if line[0] == 'L':
                number = -number
            current_position = (current_position + number) % 100
            if current_position == 0:
                zero_counter = zero_counter + 1
        return zero_counter

    def solve_bonus_task(self, input_file_content: List[str]):
        current_position = 50
        zero_counter = 0
        for line in input_file_content:
            number = int(line[1:])
            if line[0] == 'L':
                number = -number
            while number != 0:
                if number < 0:
                    current_position = (current_position - 1) % 100
                    number = number + 1
                else:
                    current_position = (current_position + 1) % 100
                    number = number - 1
                if current_position == 0:
                    zero_counter = zero_counter + 1
        return zero_counter

    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch("(R|L)[0-9]+\n?", line) for line in input_file_content)
