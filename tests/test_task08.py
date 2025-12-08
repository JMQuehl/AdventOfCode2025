from tests.abstract_test import TaskTest
import unittest
from advent_of_code_template.tasks.task08.task08 import Task08
from advent_of_code_template.advent_of_code_utils import parse_args


class Task08Tests(TaskTest, unittest.TestCase):
    task = Task08(parse_args([]))
    known_input = ["162,817,812\n",
                   "57,618,57\n",
                   "906,360,560\n",
                   "592,479,940\n",
                   "352,342,300\n",
                   "466,668,158\n",
                   "542,29,236\n",
                   "431,825,988\n",
                   "739,650,466\n",
                   "52,470,668\n",
                   "216,146,977\n",
                   "819,987,18\n",
                   "117,168,530\n",
                   "805,96,715\n",
                   "346,949,466\n",
                   "970,615,88\n",
                   "941,993,340\n",
                   "862,61,35\n",
                   "984,92,344\n",
                   "425,690,689"]
    known_output = 40
    known_bonus_output = 25272

    def test_given_example(self):
        assert self.task.solve_task(self.known_input, 10) == self.known_output
