import AI_CH3.util as util

_X_ = None


class DynamicProgrammingSearch(util.SearchAlgorithm):
    def __init__(self, memory_use=True, verbose=0):
        self.memory_use = memory_use  # memory_use: 입력안하면 자동으로 True
        if memory_use:
            self.future_dict = {}  # key: state, value: (path, cost, num_visited)
        self.verbose = verbose

    def future(self, problem, state):  # target state
        if self.memory_use and state in self.future_dict:
            actions, cost, _ = self.future_dict[
                state]  # use self.future_dict # _: 3개의 결과값 중 마지막 값은 사용하지 않는다. # [state]: 키 값만 호출
            return actions, cost, 0  # 0: 한 번 방문한 곳은 다시 방문하지 않는다

        num_visited = 1
        if problem.is_end(state):
            min_actions = []
            min_cost = 0
        else:
            min_cost = float('inf')
            min_actions = []
            for action, successor, action_cost in problem.succ_and_cost(state):
                future_actions, future_cost, future_num_visited = self.future(problem, successor)
                num_visited += future_num_visited
                cost = action_cost + future_cost
                if cost < min_cost:
                    min_actions = [action] + future_actions
                    min_cost = cost
        if self.memory_use:
            self.future_dict[state] = min_actions, min_cost, num_visited
        return min_actions, min_cost, num_visited

    def solve(self, problem):
        actions, cost, num_visited = self.future(problem, problem.start_state())
        if self.verbose >= 1:
            print("numStatesVisited = {}".format(num_visited))
            print("totalCost = {}".format(cost))
            print("actions = {}".format(actions))
        return tuple(actions), cost, num_visited