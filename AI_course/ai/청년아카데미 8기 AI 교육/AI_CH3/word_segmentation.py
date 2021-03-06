import AI_CH3.util as util
import AI_CH3.wordsegUtil as wordsegUtil

_X_ = None

class SegmentationProblem(util.SearchProblem):
    def __init__(self, query, unigramCost):
        self.query = query
        self.unigramCost = unigramCost

    def start_state(self):
        return 0  # num of characters used to construct words

    def is_end(self, state):
        return state == len(self.query)

    def succ_and_cost(self, state):
        result=[]
        for step in range(1, len(self.query) - state + 1):
            next_state = state + step
            word = self.query[state:next_state]
            cost = self.unigramCost(word)

            result.append((word, next_state, cost))  # action, next_state, cost
        return result

if __name__ == '__main__':
    #
    QUERIES_SEG = [
        'thestaffofficerandprinceandrewmountedtheirhorsesandrodeon',
        'hellothere',
        'officerandshort',
        'erprince',
        'howdythere',
        'whatsup',
        'duduandtheprince',
        'duduandtheking',
        'withoutthecourtjester',
        'lightbulbneedschange',
        'imagineallthepeople',
        'thisisnotmybeautifulhouse',
    ]
    unigramCost, bigramCost = wordsegUtil.makeLanguageModels('leo-will.txt')


    for q in QUERIES_SEG:

        problem = SegmentationProblem(q, unigramCost) # q is string that is not segmented.

        import dynamic_programming_search
        dps = dynamic_programming_search.DynamicProgrammingSearch(verbose=1)
        # dps = dynamic_programming_search.DynamicProgrammingSearch(memory_use=False, verbose=1)
        print(dps.solve(problem))

        import uniform_cost_search
        # ucs = uniform_cost_search.UniformCostSearch(verbose=0)
        # print(ucs.solve(problem))


# === Other Examples ===
#
# QUERIES_SEG = [
#     'thestaffofficerandprinceandrewmountedtheirhorsesandrodeon',
#     'hellothere',
#     'officerandshort',
#     'erprince',
#     'howdythere',
#     'whatsup',
#     'duduandtheprince',
#     'duduandtheking',
#     'withoutthecourtjester',
#     'lightbulbneedschange',
#     'imagineallthepeople',
#     'thisisnotmybeautifulhouse',
# ]
