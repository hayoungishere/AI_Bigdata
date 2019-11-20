import util
import wordsegUtil


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
        raise NotImplementedError


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
    for query, answer in zip(QUERIES_BOTH, ANSWERS * 10):
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

