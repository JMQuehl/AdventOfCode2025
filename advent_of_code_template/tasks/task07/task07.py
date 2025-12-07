from advent_of_code_template.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List
import re


class Task07(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = 'The total number of splits is: %d'
        self.bonus_answer_text = 'The total number of timelines is: %d'
        self.task_number = 7

    def solve_task(self, input_file_content: List[str]):
        input_list = [x.strip() for x in input_file_content]
        start = input_list[0].find('S')
        rays = [start]
        new_rays = []
        split_counter = 0
        for i in range(len(input_list[1:])):
            for ray in rays:
                if 0 < ray < len(input_list[i + 1]) and input_list[i + 1][ray] == '^':
                    split_counter = split_counter + 1
                    if ray - 1 not in new_rays:
                        new_rays.append(ray - 1)
                    if ray + 1 not in new_rays:
                        new_rays.append(ray + 1)
                elif ray not in new_rays:
                    new_rays.append(ray)
            rays = new_rays
            new_rays = []
        return split_counter

    def solve_bonus_task(self, input_file_content: List[str]):
        input_list = [x.strip() for x in input_file_content]
        start = input_list[0].find('S')
        rays = [0] * len(input_list[0])
        rays[start] = 1
        new_rays = [0] * len(input_list[0])
        for i in range(len(input_list[1:])):
            for j in range(len(rays)):
                if rays[j] > 0 and input_list[i + 1][j] == '^':
                    new_rays[j-1] = new_rays[j-1] + rays[j]
                    new_rays[j+1] = new_rays[j+1] + rays[j]
                    new_rays[j] = 0
                else:
                    new_rays[j] = new_rays[j] + rays[j]
            rays = new_rays
            new_rays = [0] * len(rays)
        return sum(rays)

    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch("[.^S]+\n?", line) for line in input_file_content)
