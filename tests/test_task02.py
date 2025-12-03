from tests.abstract_test import TaskTest
import unittest
from advent_of_code_template.tasks.task02.task02 import Task02
from advent_of_code_template.advent_of_code_utils import parse_args


class Task02Tests(TaskTest, unittest.TestCase):
    task = Task02(parse_args([]))
    known_input = [
        "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,"
        "446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"]
    known_output = 1227775554
    known_bonus_output = 4174379265
