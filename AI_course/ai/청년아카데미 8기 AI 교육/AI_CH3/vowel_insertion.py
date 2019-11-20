import AI_CH3.util as util
import AI_CH3.wordsegUtil as wordsegUtil

_X_ = None

class VowelInsertionProblem(util.SearchProblem):
    def __init__(self, queryWords, bigramCost, possibleFills):
        self.queryWords = queryWords
        self.bigramCost = bigramCost
        self.possibleFills = possibleFills

    def start_state(self):
        return 0, wordsegUtil.SENTENCE_BEGIN  # word position & previous reconstructed word

    def is_end(self, state):
        return state[0] == len(self.queryWords)

    def succ_and_cost(self, state):
        result=[]
        pos, prev_word =state[0], state[1]
        vowel_removed_word = self.queryWords[pos]
        fills = self.possibleFills(vowel_removed_word) | {vowel_removed_word}


        for fill in fills: # fills is action.
            next_state = (pos+1, fill, prev_word)
            cost = self.bigramCost(prev_word, fill) # 이전 단어에 비해서 얼마나 자연스러워졌는지를 확인할 수 있음.
            result.append((fill, next_state, cost))  # action, next_state, cost
        return result

if __name__ == '__main__':    
    unigramCost, bigramCost = wordsegUtil.makeLanguageModels('leo-will.txt')
    possibleFills = wordsegUtil.makeInverseRemovalDictionary('leo-will.txt', 'aeiou') # 모음을 제거한 단어들을 학습 시켜서 어떤 모음이 들어가는 것이 가장 자연스러운지를 찾아냄.
    problem = VowelInsertionProblem('thts m n th crnr'.split(), bigramCost, possibleFills)

    import dynamic_programming_search
    dps = dynamic_programming_search.DynamicProgrammingSearch(verbose=1)
    # dps = dynamic_programming_search.DynamicProgrammingSearch(memory_use=False, verbose=1)
    # print dps.solve(problem)

    import uniform_cost_search
    ucs = uniform_cost_search.UniformCostSearch(verbose=0)
    print(ucs.solve(problem))


# === Other Examples ===
# 
# QUERIES_INS = [
#     'strng',
#     'pls',
#     'hll thr',
#     'whats up',
#     'dudu and the prince',
#     'frog and the king',
#     'ran with the queen and swam with jack',
#     'light bulbs need change',
#     'ffcr nd prnc ndrw',
#     'ffcr nd shrt prnc',
#     'ntrntnl',
#     'smthng',
#     'btfl',
# ]
