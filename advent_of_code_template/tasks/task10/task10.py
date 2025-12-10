from advent_of_code_template.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List
import re
from collections import deque
import pulp


def press_button(state: str, button: List[int]) -> str:
    new_state = [x for x in state]
    for num in button:
        if new_state[num] == '.':
            new_state[num] = '#'
        else:
            new_state[num] = '.'
    return "".join(new_state)


def press_button_bonus_task(state: List[int], button: List[int]) -> List[int]:
    new_state = state.copy()
    for num in button:
        new_state[num] = new_state[num] + 1
    return new_state


class Task10(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = 'The number of buttons you have to press to reach each target is: %d'
        self.bonus_answer_text = 'The number of buttons you have to press to reach the counter values is: %d'
        self.task_number = 10

    def solve_task(self, input_file_content: List[str]):
        toggle_sum = 0
        for line in input_file_content:
            target = line.split()[0][1:-1]
            state = '.' * len(target)
            buttons = [[int(y) for y in x[1:-1].split(',')] for x in line.split()[1:-1]]
            search_space = deque([(state, [])])
            found_solution = False
            while not found_solution:
                current_state = search_space.popleft()
                for button in [x for x in buttons if x not in current_state[1]]:
                    result = press_button(current_state[0], button)
                    if result == target:
                        toggle_sum = toggle_sum + len(current_state[1]) + 1
                        found_solution = True
                        break
                    else:
                        new_button_presses = current_state[1].copy() + [button]
                        search_space.append((result, new_button_presses))

        return toggle_sum

    def solve_bonus_task(self, input_file_content: List[str]):
        toggle_sum = 0
        for line in input_file_content:
            target = [int(x) for x in line.strip().split()[-1][1:-1].split(',')]
            buttons = [[int(y) for y in x[1:-1].split(',')] for x in line.split()[1:-1]]

            problem = pulp.LpProblem("Counter_Configuration", pulp.LpMinimize)

            x_vars = [pulp.LpVariable(f'x_{j}', lowBound=0, cat='Integer') for j in range(len(buttons))]

            problem += pulp.lpSum(x_vars), "Total_Toggles"

            for i in range(len(target)):
                constraint_expr = pulp.lpSum(x_vars[j] for j in range(len(buttons)) if i in buttons[j])
                problem += constraint_expr == target[i], f"Counter_{i}"

            solver = pulp.PULP_CBC_CMD(msg=False)
            problem.solve(solver)

            if pulp.LpStatus[problem.status] == 'Optimal':
                toggle_sum += sum(int(pulp.value(var)) for var in x_vars)
        return toggle_sum

    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch("\[[.#]+\] (\([0-9]+(,[0-9]+)*\) )+\{[0-9]+(,[0-9]+)+\}\n?", line) for line in
                   input_file_content)
