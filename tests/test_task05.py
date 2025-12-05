from tests.abstract_test import TaskTest
import unittest
from advent_of_code_template.tasks.task05.task05 import Task05
from advent_of_code_template.advent_of_code_utils import parse_args


class Task05Tests(TaskTest, unittest.TestCase):
    task = Task05(parse_args([]))
    known_input = ["3-5\n",
                   "10-14\n",
                   "16-20\n",
                   "12-18\n",
                   "\n",
                   "1\n",
                   "5\n",
                   "8\n",
                   "11\n",
                   "17\n",
                   "32\n"]
    known_output = 3
    known_bonus_output = 14
