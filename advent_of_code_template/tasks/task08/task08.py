from math import sqrt

from advent_of_code_template.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List
import re


class BreakerNode:
    circuit: int = -1

    def __init__(self, ):
        pass


class Task08(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = 'After 1000 connections, the product of cluster sizes is: %d'
        self.bonus_answer_text = 'The result based on the last two connected breakers is: %d'
        self.task_number = 8

    def solve_task(self, input_file_content: List[str], n=1000):
        # a node is a list of 3 coordinates
        nodes = [[int(y) for y in x.strip().split(',')] for x in input_file_content]
        clusters: List[List[int]] = []
        distances = []  # node1, node2, distance
        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                distances.append((i, j, sqrt((nodes[i][0] - nodes[j][0]) ** 2 + (nodes[i][1] - nodes[j][1]) ** 2 + (
                        nodes[i][2] - nodes[j][2]) ** 2)))
        distances.sort(key=lambda x: x[2])

        for i in range(n):
            current_distance = distances[0]
            first_cluster = -1
            second_cluster = -1
            for j, cluster in enumerate(clusters):
                if current_distance[0] in cluster:
                    first_cluster = j
                if current_distance[1] in cluster:
                    second_cluster = j
                if first_cluster >= 0 and second_cluster >= 0:
                    break
            if first_cluster >= 0 and second_cluster >= 0:  # two clusters found
                if first_cluster != second_cluster:
                    clusters[first_cluster].extend(clusters[second_cluster])
                    clusters = clusters[:second_cluster] + clusters[second_cluster + 1:]
            elif first_cluster >= 0:  # add second node to cluster of first
                clusters[first_cluster].append(current_distance[1])
            elif second_cluster >= 0:  # add first node to cluster of second
                clusters[second_cluster].append(current_distance[0])
            else:  # create new cluster
                clusters.append([current_distance[0], current_distance[1]])
            distances = distances[1:]
        clusters.sort(key=lambda x: len(x), reverse=True)
        return len(clusters[0]) * len(clusters[1]) * len(clusters[2])

    def solve_bonus_task(self, input_file_content: List[str]):
        # a node is a list of 3 coordinates
        nodes = [[int(y) for y in x.strip().split(',')] for x in input_file_content]
        clusters: List[List[int]] = []
        distances = []  # node1, node2, distance
        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                distances.append((i, j, sqrt((nodes[i][0] - nodes[j][0]) ** 2 + (nodes[i][1] - nodes[j][1]) ** 2 + (
                        nodes[i][2] - nodes[j][2]) ** 2)))
        distances.sort(key=lambda x: x[2])

        done = False
        last_x = -1
        last_x2 = -1

        while not done:
            current_distance = distances[0]
            last_x = nodes[current_distance[0]][0]
            last_x2 = nodes[current_distance[1]][0]
            first_cluster = -1
            second_cluster = -1
            for j, cluster in enumerate(clusters):
                if current_distance[0] in cluster:
                    first_cluster = j
                if current_distance[1] in cluster:
                    second_cluster = j
                if first_cluster >= 0 and second_cluster >= 0:
                    break
            if first_cluster >= 0 and second_cluster >= 0:  # two clusters found
                if first_cluster != second_cluster:
                    clusters[first_cluster].extend(clusters[second_cluster])
                    clusters = clusters[:second_cluster] + clusters[second_cluster + 1:]
            elif first_cluster >= 0:  # add second node to cluster of first
                clusters[first_cluster].append(current_distance[1])
            elif second_cluster >= 0:  # add first node to cluster of second
                clusters[second_cluster].append(current_distance[0])
            else:  # create new cluster
                clusters.append([current_distance[0], current_distance[1]])
            distances = distances[1:]
            done = len(clusters) == 1 and len(clusters[0]) == len(nodes)
        clusters.sort(key=lambda x: len(x), reverse=True)
        return last_x * last_x2

    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch("([0-9]+,)+[0-9]+\n?", line) for line in input_file_content)
