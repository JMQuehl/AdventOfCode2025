from tests.abstract_test import TaskTest
import unittest
from advent_of_code_template.tasks.task09.task09 import Task09
from advent_of_code_template.advent_of_code_utils import parse_args


class Task09Tests(TaskTest, unittest.TestCase):
    task = Task09(parse_args([]))
    known_input = ["7,1\n",
                   "11,1\n",
                   "11,7\n",
                   "9,7\n",
                   "9,5\n",
                   "2,5\n",
                   "2,3\n",
                   "7,3"]
    known_output = 50
    known_bonus_output = 24
