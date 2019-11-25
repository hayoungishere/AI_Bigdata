import AI_CH3.util as util
import AI_CH3.wordsegUtil as wordsegUtil

_X_ = None

class JointSegmentationInsertionProblem(util.SearchProblem):
    def __init__(self, query, bigramCost, possibleFills):
        self.query = query
        self.bigramCost = bigramCost
        self.possibleFills = possibleFills

    def start_state(self):
        # position before which text is reconstructed & previous word
        return 0, wordsegUtil.SENTENCE_BEGIN

    def is_end(self, state):
        return state[0] == len(self.query)

    def succ_and_cost(self, state):
        results = []
        position, prev_word = state
        for l in range(1, len(self.query) - position + 1):
            candidate_words = self.possibleFills(self.query[position:position+l])
            # 현재 위치 ~ 확인가능한 모든 위치까지 모음을 추가한 것을 candidate_words에 저장.
            for word in candidate_words:
                action = word
                new_state = (position+l, word)
                # state를 새로운 위치 position+l과 그 때의 candidate_word로 update 한다.
                cost = self.bigramCost(prev_word, word)
                results.append((action, new_state, cost))
                # candidate word와 새로운 state, 앞단어와 얼마나 자연스럽게 연결되는지를 저장한 cost를 다음 state로 넘겨준다.
        return results


# === Other Examples ===

QUERIES_BOTH = [
    'stff',
    'hllthr',
    'thffcrndprncndrw',
    'thstffffcrndprncndrwmntdthrhrssndrdn',
    'whatsup',
    'ipovercarrierpigeon',
    'aeronauticalengineering',
    'themanwiththegoldeneyeball',
    'lightbulbsneedchange',
    'internationalplease',
    'comevisitnaples',
    'somethingintheway',
    'itselementarymydearwatson',
    'itselementarymyqueen',
    'themanandthewoman',
    'nghlrdy',
    'jointmodelingworks',
    'jointmodelingworkssometimes',
    'jointmodelingsometimesworks',
    'rtfclntllgnc',
]

ANSWERS = [
    (['staff'], 9.599717951117373, 9),
    (['hill', 'there'], 17.813677434340605, 37),
    (['the', 'officer', 'and', 'prince', 'andrew'], 30.81585916904296, 183),
    (['the', 'staff', 'officer', 'and', 'prince', 'andrew', 'mounted', 'their', 'horses', 'under', 'done'], 86.06390603257708, 820),
    (['whats', 'up'], 17.302219600268685, 34),
    (['pauvre', 'carrier', 'up', 'again'], 41.70338234778151, 154),
    (['arent', 'clean', 'ignoring'], 35.730460348915365, 159),
    (['the', 'man', 'with', 'the', 'golden', 'eyeball'], 46.62296979525153, 300),
    (['light', 'blue', 'bees', 'and', 'change'], 46.34303180663817, 170),
    (['international', 'please'], 22.1209190726572, 142),
    (['come', 'visit', 'naples'], 30.65019409644063, 82),
    (['something', 'in', 'the', 'way'], 26.1882312269055, 165),
    (['its', 'elementary', 'my', 'drew', 'its', 'in'], 52.493205313403315, 334),
    (['its', 'elementary', 'my', 'queen'], 40.82587095970001, 231),
    (['the', 'man', 'and', 'the', 'woman'], 30.224084109812544, 186),
    (['enough', 'already'], 19.419253942549496, 31),
    (['joint', 'modeling', 'works'], 36.566329298584535, 163),
    (['joint', 'modeling', 'works', 'sometimes'], 46.536617692182155, 231),
    (['joint', 'modeling', 'sometimes', 'works'], 46.53662548330286, 254),
    (['artificial', 'intelligence'], 23.92860546337033, 87)
]

if __name__ == '__main__':
    unigramCost, bigramCost = wordsegUtil.makeLanguageModels('leo-will.txt')
    smoothCost = wordsegUtil.smoothUnigramAndBigram(unigramCost, bigramCost, 0.2)
    possibleFills = wordsegUtil.makeInverseRemovalDictionary('leo-will.txt', 'aeiou')

    # import dynamic_programming_search
    # dps = dynamic_programming_search.DynamicProgrammingSearch(verbose=1)
    # dps = dynamic_programming_search.DynamicProgrammingSearch(memory_use=False, verbose=1)

    import uniform_cost_search
    ucs = uniform_cost_search.UniformCostSearch(verbose=0)

    num_wrong_pred = 0
    for query, answer in zip(QUERIES_BOTH, ANSWERS):
        problem = JointSegmentationInsertionProblem(wordsegUtil.removeAll(query, 'aeiou'), smoothCost, possibleFills)
        prediction = ucs.solve(problem)
        # print(prediction)
        if all([prediction[0] == answer[0],
                abs(answer[1] - prediction[1]) < 0.1]):
            print('[Correct prediction]')
        else:
            num_wrong_pred += 1
            print('[Wrong prediction]')
        print('Prediction: {}'.format(prediction))
        print('Answer: {}'.format(answer))
        print()
    print('Total of {} wrong predictions'.format(num_wrong_pred))
