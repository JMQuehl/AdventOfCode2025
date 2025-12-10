from tests.abstract_test import TaskTest
import unittest
from advent_of_code_template.tasks.task10.task10 import Task10
from advent_of_code_template.advent_of_code_utils import parse_args


class Task10Tests(TaskTest, unittest.TestCase):
    task = Task10(parse_args([]))
    known_input = ["[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}\n",
                   "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}\n",
                   "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"]
    known_output = 7
    known_bonus_output = 33
