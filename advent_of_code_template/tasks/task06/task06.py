from advent_of_code_template.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List
import re


def custom_split(input_list: List[str]) -> List[List[str]]:
    split_indexes = []
    for i in range(len(input_list[0])):
        if all([x[i] == ' ' for x in input_list]):
            split_indexes.append(i)
    split_lines = [[] for _ in range(len(input_list))]
    start = 0
    for index in split_indexes:
        for i, line in enumerate(input_list):
            split_lines[i].append(line[start:index])
        start = index + 1
    for i, line in enumerate(input_list):
        split_lines[i].append(line[start:].replace("\n", ""))
    return split_lines

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
        operators = input_file_content[-1].split()
        number_lines = input_file_content[:-1]
        split_lines = custom_split(number_lines)
        results = []
        for i, op in enumerate(operators): # for each block
            numbers = [[] for _ in range(len(split_lines[0][i]))]
            for j in range(len(split_lines[0][i])):
                for k in range(len(split_lines)):
                    numbers[j].append(split_lines[k][i][j])
            numbers_int = [int(''.join(x).strip()) for x in numbers]
            current_result = numbers_int[0]
            for number in numbers_int[1:]:
                if op == '*':
                    current_result = current_result * number
                else:
                    current_result = current_result + number
            results.append(current_result)
        return sum(results)

    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch("(( *([+*] *)+)|( *[0-9]+ *)+)\n?", line) for line in input_file_content)
