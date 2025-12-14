from tests.abstract_test import TaskTest
import unittest
from advent_of_code_template.tasks.task11.task11 import Task11
from advent_of_code_template.advent_of_code_utils import parse_args


class Task11Tests(TaskTest, unittest.TestCase):
    task = Task11(parse_args([]))
    known_input = ["aaa: you hhh\n",
                   "you: bbb ccc\n",
                   "bbb: ddd eee\n",
                   "ccc: ddd eee fff\n",
                   "ddd: ggg\n",
                   "eee: out\n",
                   "fff: out\n",
                   "ggg: out\n",
                   "hhh: ccc fff iii\n",
                   "iii: out"]
    known_output = 5
    known_bonus_input = ["svr: aaa bbb\n",
                         "aaa: fft\n",
                         "fft: ccc\n",
                         "bbb: tty\n",
                         "tty: ccc\n",
                         "ccc: ddd eee\n",
                         "ddd: hub\n",
                         "hub: fff\n",
                         "eee: dac\n",
                         "dac: fff\n",
                         "fff: ggg hhh\n",
                         "ggg: out\n",
                         "hhh: out"]
    known_bonus_output = 2

    def test_given_bonus_example(self):
        assert self.task.solve_bonus_task(self.known_bonus_input) == self.known_bonus_output
