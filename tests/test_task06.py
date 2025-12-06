from tests.abstract_test import TaskTest
import unittest
from advent_of_code_template.tasks.task06.task06 import Task06
from advent_of_code_template.advent_of_code_utils import parse_args


class Task06Tests(TaskTest, unittest.TestCase):
    task = Task06(parse_args([]))
    known_input = ["123 328  51 64 \n",
                   " 45 64  387 23 \n",
                   "  6 98  215 314\n",
                   "*   +   *   +  \n"]
    known_output = 4277556
    known_bonus_output = -1
