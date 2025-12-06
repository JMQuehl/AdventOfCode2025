from advent_of_code_template.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List
import re


class Task06(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = 'The sum of all results is: %d'
        self.bonus_answer_text = 'The new sum of all results is: %d'
        self.task_number = 6

    def solve_task(self, input_file_content: List[str]):
        number_lines = [[int(y) for y in x.split()] for x in input_file_content[:-1]]
        operators = input_file_content[-1].split()
        results = number_lines[0]

        for number_line in number_lines[1:]:
            for i, op in enumerate(operators):
                if op == '*':
                    results[i] = results[i] * number_line[i]
                else:
                    results[i] = results[i] + number_line[i]
        return sum(results)

    def solve_bonus_task(self, input_file_content: List[str]):
        return -1

    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch("(( *([+*] *)+)|( *[0-9]+ *)+)\n?", line) for line in input_file_content)
