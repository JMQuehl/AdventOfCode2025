from tests.abstract_test import TaskTest
import unittest
from advent_of_code_template.tasks.task01.task01 import Task01
from advent_of_code_template.advent_of_code_utils import parse_args


class Task01Tests(TaskTest, unittest.TestCase):
    task = Task01(parse_args([]))
    known_input = ["L68\n",
                   "L30\n",
                   "R48\n",
                   "L5\n",
                   "R60\n",
                   "L55\n",
                   "L1\n",
                   "L99\n",
                   "R14\n",
                   "L82"]
    known_output = 3
    known_bonus_output = -1
