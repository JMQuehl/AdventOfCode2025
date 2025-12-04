from advent_of_code_template.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List
import re


class Task02(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = 'The sum of invalid numbers is: %d'
        self.bonus_answer_text = 'The new sum of invalid numbers is: %d'
        self.task_number = 2

    def solve_task(self, input_file_content: List[str]):
        ranges = input_file_content[0].split(',')
        invalid_sum = 0
        for range_str in ranges:
            lower, upper = [int(x) for x in range_str.split('-')]
            for i in range(lower, upper + 1):
                string_repr = str(i)
                s1, s2 = string_repr[:len(string_repr)//2], string_repr[len(string_repr)//2:]
                if s1 == s2:
                    invalid_sum = invalid_sum + i
        return invalid_sum

    def solve_bonus_task(self, input_file_content: List[str]):
        ranges = input_file_content[0].split(',')
        invalid_sum = 0
        for range_str in ranges:
            lower, upper = [int(x) for x in range_str.split('-')]
            for i in range(lower, upper + 1):
                string_repr = str(i)
                for j in range(1, len(string_repr)//2 + 1):
                    if len(string_repr) % j == 0:
                        substr = string_repr[:j]
                        if substr * (len(string_repr) // j) == string_repr:
                            invalid_sum = invalid_sum + i
                            break
        return invalid_sum

    def is_input_valid(self, input_file_content: List[str]):
        pattern = '([0-9]+-[0-9]+,)*([0-9]+-[0-9]+)+\n?'
        return len(input_file_content) == 1 and re.fullmatch(pattern, input_file_content[0])
