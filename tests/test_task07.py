from tests.abstract_test import TaskTest
import unittest
from advent_of_code_template.tasks.task07.task07 import Task07
from advent_of_code_template.advent_of_code_utils import parse_args


class Task07Tests(TaskTest, unittest.TestCase):
    task = Task07(parse_args([]))
    known_input = [".......S.......\n",
                   "...............\n",
                   ".......^.......\n",
                   "...............\n",
                   "......^.^......\n",
                   "...............\n",
                   ".....^.^.^.....\n",
                   "...............\n",
                   "....^.^...^....\n",
                   "...............\n",
                   "...^.^...^.^...\n",
                   "...............\n",
                   "..^...^.....^..\n",
                   "...............\n",
                   ".^.^.^.^.^...^.\n",
                   "..............."]
    known_output = 21
    known_bonus_output = 40
