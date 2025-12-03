from tests.abstract_test import TaskTest
import unittest
from advent_of_code_template.tasks.task03.task03 import Task03
from advent_of_code_template.advent_of_code_utils import parse_args


class Task03Tests(TaskTest, unittest.TestCase):
    task = Task03(parse_args([]))
    known_input = ["987654321111111\n",
                   "811111111111119\n",
                   "234234234234278\n",
                   "818181911112111\n"]
    known_output = 357
    known_bonus_output = 3121910778619
