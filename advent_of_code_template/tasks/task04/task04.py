from advent_of_code_template.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List
import re


def expand_board(input_list: List[str]) -> List[str]:
    clone = ['.' + x.strip() + '.' for x in input_list]
    clone = ['.' * len(clone[0])] + clone
    clone.append('.' * len(clone[0]))
    return clone


def count_neighbors(input_file_content, i, j) -> int:
    num_neighbors = 0
    num_neighbors = num_neighbors + input_file_content[i-1][j-1:j+2].count('@')
    num_neighbors = num_neighbors + input_file_content[i][j-1:j+2].count('@') - 1 # i,j is not counted
    num_neighbors = num_neighbors + input_file_content[i + 1][j - 1:j + 2].count('@')
    return num_neighbors


class Task04(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = 'The number of rolls that can be accessed is: %d'
        self.bonus_answer_text = 'The number of rolls that can be removed is: %d'
        self.task_number = 4

    def solve_task(self, input_file_content: List[str]):
        board = expand_board(input_file_content)
        count_reachable = 0
        for i, line in enumerate(board):
            for j, sign in enumerate(line):
                if sign == '@':
                    if count_neighbors(board, i, j) < 4:
                        count_reachable = count_reachable + 1
        return count_reachable

    def solve_bonus_task(self, input_file_content: List[str]):
        board = expand_board(input_file_content)
        count_removed = 0
        done = False
        while not done:
            done = True # will be set to false if any changes occur
            for i, line in enumerate(board):
                for j in range(len(line)):
                    sign = board[i][j]
                    if sign == '@':
                        if count_neighbors(board, i, j) < 4:
                            count_removed = count_removed + 1
                            board[i] = board[i][:j] + '.' + board[i][j+1:]
                            done = False
        return count_removed

    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch("[.@]+\n?", line) for line in input_file_content)
