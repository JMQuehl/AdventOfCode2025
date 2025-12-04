from tests.abstract_test import TaskTest
import unittest
from advent_of_code_template.tasks.task04.task04 import Task04
from advent_of_code_template.advent_of_code_utils import parse_args


class Task04Tests(TaskTest, unittest.TestCase):
    task = Task04(parse_args([]))
    known_input = ["..@@.@@@@.",
                   "@@@.@.@.@@",
                   "@@@@@.@.@@",
                   "@.@@@@..@.",
                   "@@.@@@@.@@",
                   ".@@@@@@@.@",
                   ".@.@.@.@@@",
                   "@.@@@.@@@@",
                   ".@@@@@@@@.",
                   "@.@.@@@.@."]
    known_output = 13
    known_bonus_output = 43
