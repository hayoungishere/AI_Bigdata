import game
import random

#==========================================================
# MinimaxAgent class
#==========================================================

class MinimaxAgent:
    def V(self, state):
        # BEGIN_YOUR_CODE
        if game.is_end(state):
            return game.utility(state)

        if game.get_player_from_state(state) == game.MAX_PLAYER:  # my-turn
            value = -game.INT_INF
            for action in game.get_possible_actions(state):
                value = max(value, self.V(game.get_next_state(state, action)))
        else:  # opp-turn
            value = game.INT_INF
            for action in game.get_possible_actions(state):
                value = min(value, self.V(game.get_next_state(state, action)))

        return value
        # END_YOUR_CODE

    def policy(self, state):
        actions = game.get_possible_actions(state)
        assert len(actions) > 0

        optimal = max if game.get_player_from_state(state) == game.MAX_PLAYER else min
        return optimal(actions, key=lambda x: self.V(game.get_next_state(state, x)))

#==========================================================
# Alpha-beta Pruning class
#==========================================================

class PruningMinimaxAgent:
    def V(self, state, alpha=-game.INT_INF, beta=game.INT_INF):
        # BEGIN_YOUR_CODE
        if game.is_end(state):
            return game.utility(state)

        actions = game.get_possible_actions(state)
        if game.get_player_from_state(state) == game.MAX_PLAYER:  # my-turn
            value = -game.INT_INF
            for action in actions:
                value = max(value, self.V(game.get_next_state(state, action)))
        else:  # opp-turn
            value = 0
            for action in actions:
                value += self.V(game.get_next_state(state, action)) / len(actions)

        return value
        # END_YOUR_CODE

    def policy(self, state):
        actions = game.get_possible_actions(state)
        assert len(actions) > 0

        alpha = -game.INT_INF
        beta = game.INT_INF

        if game.get_player_from_state(state) == game.MAX_PLAYER:
            values = []
            for action in actions:
                value = self.V(game.get_next_state(state, action), alpha, beta)
                values.append(value)
                alpha = max(alpha, value)
            return max(list(zip(actions, values)), key=lambda x: x[1])[0]
        else:
            values = []
            for action in actions:
                value = self.V(game.get_next_state(state, action), alpha, beta)
                values.append(value)
                beta = min(beta, value)
            return min(list(zip(actions, values)), key=lambda x: x[1])[0]

#==========================================================
# DepthLimitedMinimaxAgent class
#==========================================================

heuristic_array = [
    [  0, -10, -100, -1000],
    [  10,  0,    0,     0],
    [ 100,  0,    0,     0],
    [1000,  0,    0,     0]
]

def eval(state):
    result = 0
    for cond in game.WIN_CONDITIONS:
        maxs = mins = 0
        for loc in cond:
            if state[loc] == game.MAX_PLAYER:
                maxs += 1
            elif state[loc] == game.MIN_PLAYER:
                mins += 1
        result += heuristic_array[maxs][mins]

    return result

class DepthLimitedMinimaxAgent:
    def __init__(self, max_depth=2):
        self.max_depth = max_depth

    def V(self, state, depth):
        # BEGIN_YOUR_CODE
        if game.is_end(state):
            return game.utility(state)
        if depth ==0:
            return eval(state)

        if game.get_player_from_state(state) == game.MAX_PLAYER:  # my-turn
            value = -game.INT_INF
            for action in game.get_possible_actions(state):
                value = max(value, self.V(game.get_next_state(state, action),depth))
        else:  # opp-turn
            value = game.INT_INF
            for action in game.get_possible_actions(state):
                value = min(value, self.V(game.get_next_state(state, action), depth-1))

        return value
        # END_YOUR_CODE

    def policy(self, state):
        actions = game.get_possible_actions(state)
        assert len(actions) > 0

        optimal = max if game.get_player_from_state(state) == game.MAX_PLAYER else min
        return optimal(actions, key=lambda x: self.V(game.get_next_state(state, x), self.max_depth))
