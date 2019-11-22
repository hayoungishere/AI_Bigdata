import AI_CH4.util as util
import math, random
from collections import defaultdict
from AI_CH4.util import ValueIteration

############################################################
# Problem A

class ExampleMDP(util.MDP):
    def startState(self):
        return 0

    # Return set of actions possible from |state|.
    def actions(self, state):
        return ['Left', 'Right']

    # Return a list of (newState, prob, reward) tuples corresponding to edges
    # coming out of |state|.
    def succAndProbReward(self, state, action):
        if state == -2 or state == 2:
            # Check isEnd
            return []
        
        leftReward = -5 # default reward of left_side
        rightReward = -5 # default reward of right_side

        if state - 1 == -2: # state - 1  means current position's left side
            leftReward = 20
        if state + 1 == 2: # state + 1 means current position's right side
            rightReward = 100
        
        if action == 'Left':
            results = [(state-1, 0.8, leftReward), (state+1, 0.2, rightReward)]
        elif  action == 'Right':
            results = [(state-1, 0.7, leftReward), (state+1, 0.3, rightReward)]
        else:
            results = []
        
        return results
            
    def discount(self):
        return 1

'''
print('\n========== Problem A ==========')
mdp = ExampleMDP() # make instance
algorithm = ValueIteration()
algorithm.solve(mdp, 20, verbose=True) # for just 2 iterations
for i in [-2, -1, 0, 1, 2]:
    print ("Value of the state '%d' : %f"%(i, algorithm.V[i])) # V[i] is dictionary key : state, value : value of each actions and state
for i in [-1, 0, 1]:
    print("Policy at the state '%d' : %s"%(i, algorithm.pi[i])) # pi[i] is dictionary key :state, value : optimal policy

print('\n end -----------------------------------------------------------')
algorithm.solve(mdp, verbose=True)
for i in [-2, -1, 0, 1, 2]:
    print ("Value of the state '%d' : %f"%(i, algorithm.V[i])) # V[i] is dictionary key : state, value : value of each actions and state
for i in [-1, 0, 1]:
    print("Policy at the state '%d' : %s"%(i, algorithm.pi[i])) # pi[i] is dictionary key :state, value : optimal policy
'''

############################################################
# Problem C

class BlackjackMDP(util.MDP):
    def __init__(self, cardValues, multiplicity, threshold, peekCost):
        """
        cardValues: array of card values for each card type
        multiplicity: number of each card type
        threshold: maximum total before going bust
        peekCost: how much it costs to peek at the next card
        """
        self.cardValues = cardValues
        self.multiplicity = multiplicity
        self.threshold = threshold
        self.peekCost = peekCost

    # Return the start state.
    # Look at this function to learn about the state representation.
    # The first element of the tuple is the sum of the cards in the player's
    # hand.
    # The second element is the index (not the value) of the next card, if the player peeked in the
    # last action.  If they didn't peek, this will be None.
    # The final element is the current deck.
    def startState(self):
        return (0, None, (self.multiplicity,) * len(self.cardValues))  # total, next card (if any), multiplicity for each card

    # Return set of actions possible from |state|.
    # You do not need to modify this function.
    # All logic for dealing with end states should be done in succAndProbReward
    def actions(self, state):
        return ['Take', 'Peek', 'Quit']

    # Return a list of (newState, prob, reward) tuples corresponding to edges
    # coming out of |state|.  Indicate a terminal state (after quitting or
    # busting) by setting the deck to None. 
    # When the probability is 0 for a particular transition, don't include that 
    # in the list returned by succAndProbReward.
    def succAndProbReward(self, state, action):
        # BEGIN_YOUR_CODE

        sumValue, peekIndex, deckState = state

        # step1. 종료 조건인지 확인하기
        if deckState is None :
            return []

        result = []

        if action == "Take":
            if peekIndex is None:
                for cardindex, cardCount in enumerate(deckState):

                    if cardCount==0:
                        continue

                    deckList = list(deckState)
                    deckList[cardindex]-=1
                    deckTuple = tuple(deckList)

                    newValue = sumValue + self.cardValues[cardindex]
                    prob = cardCount/sum(deckState)
                    reward =0

                    if newValue > self.threshold:
                        deckTuple=None
                    elif sum(deckTuple) ==0 :
                        deckTuple=None; reward = newValue


                    nextState = (newValue,None,deckTuple)
                    result.append((nextState, prob, reward))


            else:
                    # existing peekIndex
                    # update deck state
                deckList = list(deckState)
                deckList[peekIndex] -= 1
                deckTuple = tuple(deckList)
                newValue = sumValue + self.cardValues[peekIndex]

                prob = 1
                reward = 0

                if newValue > self.threshold:
                    deckTuple=None
                elif sum(deckTuple) == 0 :
                    deckTuple=None; reward=newValue

                nextState=(newValue,None,deckTuple)
                result.append((nextState, prob, reward))


        elif action =="Peek":
            sumValue, peekIndex, deckState = state

            if peekIndex is None:
                for cardIndex, cardCount in enumerate(deckState):
                    if cardCount==0 :
                        continue
                    prob = cardCount/sum(deckState)
                    nextState=(sumValue, cardIndex, deckState)
                    reward = -self.peekCost

                    result. append ((nextState, prob, reward))

        elif action == "Quit":
            nextState=(sumValue, peekIndex, None)
            prob=1
            reward = sumValue
            result.append((nextState, prob, reward))


        return result
        # END_YOUR_CODE

    def discount(self):
        return 1

'''
print('\n========== Problem C ==========')
mdp1 = BlackjackMDP(cardValues=[1, 5], multiplicity=2, threshold=10, peekCost=1)
startState = mdp1.startState()
preBustState = (6, None, (1, 1))
postBustState = (11, None, None)

mdp2 = BlackjackMDP(cardValues=[1, 5], multiplicity=2, threshold=15, peekCost=1)
preEmptyState = (11, None, (1,0))
'''
'''
print('\n---------- Test c1 ----------')
# Make sure the succAndProbReward function is implemented correctly.

vanilla_tests = [
    ([((1, None, (1, 2)), 0.5, 0), ((5, None, (2, 1)), 0.5, 0)], mdp1, startState, 'Take'),
    ([((0, None, None), 1, 0)], mdp1, startState, 'Quit'),
    ([((7, None, (0, 1)), 0.5, 0), ((11, None, None), 0.5, 0)], mdp1, preBustState, 'Take'),
    ([], mdp1, postBustState, 'Take'),
    ([], mdp1, postBustState, 'Quit'),
    ([((12, None, None), 1., 12)], mdp2, preEmptyState, 'Take'),
]

print('Vanilla Blackjack')
for no, (answer, mdp, state, action) in enumerate(vanilla_tests):
    print('No %d'%(no+1), end=' ')
    if answer != mdp.succAndProbReward(state, action):
        print('=> wrong')
    else:
        print('=> right')
    print('- state: {}, action: {}'.format(state, action))
    print('- true answer =', answer)
    print('- your answer =', mdp.succAndProbReward(state, action))
'''
"""
print('\n---------- Test c2 ----------')
peek_tests = [
    ([((0, 0, (2, 2)), 0.5, -1), ((0, 1, (2, 2)), 0.5, -1)], mdp1, startState, 'Peek'),
    ([((1 , None, (1, 2) ), 1, 0)] , mdp1, (0, 0, (2, 2)), 'Take'),
    ([], mdp1, postBustState, 'Peek'),
]

print('Peeking Blackjack')
for no, (answer, mdp, state, action) in enumerate(peek_tests):
    print('No %d'%(no+1), end=' ')
    if answer != mdp.succAndProbReward(state, action):
        print('=> wrong')
    else:
        print('=> right')
    print('- state: {}, action: {}'.format(state, action))
    print('- true answer =', answer)
    print('- your answer = ', mdp.succAndProbReward(state, action))
"""
'''
print('\n---------- Test c3 ----------')
algorithm = ValueIteration()
algorithm.solve(mdp1, verbose=True)
for s in algorithm.V:
    print('V(%s) = %f'%(s, algorithm.V[s]))
print('------------')
for s in algorithm.pi:
    print('pi(%s) = %s'%(s, algorithm.pi[s]))
print('------------')
print('Q1 (6, None, (1, 1) => %s'%(algorithm.pi[(6, None, (1, 1))]))
print('Q2 (6, 0, (1, 1) => %s'%(algorithm.pi[(6, 0, (1, 1))]))
'''
############################################################

# Problem D: Q learning

# Performs Q-learning.  Read util.RLAlgorithm for more information.
# actions: a function that takes a state and returns a list of actions.
# discount: a number between 0 and 1, which determines the discount factor
# featureExtractor: a function that takes a state and action and returns a list of (feature name, feature value) pairs.
# explorationProb: the epsilon value indicating how frequently the policy
# returns a random action
class QLearningAlgorithm(util.RLAlgorithm):
    def __init__(self, actions, discount, featureExtractor, explorationProb=0.2):
        self.actions = actions
        self.discount = discount
        self.featureExtractor = featureExtractor #(feature, value)
        self.explorationProb = explorationProb
        self.weights = defaultdict(float) # key : feature, value : weight
        self.numIters = 0

    # Return the Q function associated with the weights and features
    def getQ(self, state, action):
        score = 0
        for f, v in self.featureExtractor(state, action):
            score += self.weights[f] * v #inner product
        return score

    # This algorithm will produce an action given a state.
    # Here we use the epsilon-greedy algorithm: with probability
    # |explorationProb|, take a random action.
    def getAction(self, state):
        self.numIters += 1
        if random.random() < self.explorationProb:
            return random.choice(self.actions(state))
        else:
            return max((self.getQ(state, action), action) for action in self.actions(state))[1]

    # Call this function to get the step size to update the weights.
    def getStepSize(self):
        return 1.0 / math.sqrt(self.numIters)

    # We will call this function with (s, a, r, s'), which you should use to update |weights|.
    # Note that if s is a terminal state, then s' will be None.  Remember to check for this.
    # You should update the weights using self.getStepSize(); use
    # self.getQ() to compute the current estimate of the parameters.
    def incorporateFeedback(self, state, action, reward, newState):
        # BEGIN_YOUR_CODE (our solution is 12 lines of code, but don't worry if you deviate from this)

        if newState is None:
            vOpt=0
        else:
            vOpt = max(self.getQ(newState,a) for a in self.actions(newState)) # next step's q value

        error = self.getQ(state,action)-(self.discount*vOpt+reward)
        phi = self.featureExtractor(state,action) # feature vector

        for feature, value in phi:
            self.weights[feature]-=self.getStepSize()*error*value

        # END_YOUR_CODE

# Return a singleton list containing indicator feature for the (state, action)
# pair.  Provides no generalization.
def identityFeatureExtractor(state, action):
    featureKey = (state, action)
    featureValue = 1
    return [(featureKey, featureValue)]

'''
print('\n========== Problem D ==========')
mdp = util.NumberLineMDP()
rl = QLearningAlgorithm(mdp.actions, mdp.discount(), identityFeatureExtractor, 0)

# We call this here so that the stepSize will be 1
rl.numIters = 1

rl.incorporateFeedback(0, 1, 0, 1)
print('Incorporate the feedback of (s=0, a=1, r=0, s\'=1)')
print('Q-value for (state = 0, action = -1) : Answer %.1f, Output %.1f'%(0, rl.getQ(0, -1)))
print('Q-value for (state = 0, action =  1) : Answer %.1f, Output %.1f'%(0, rl.getQ(0, 1)))

rl.incorporateFeedback(1, 1, 1, 2)
print('Incorporate the feedback of (s=1, a=1, r=1, s\'=2)')
print('Q-value for (state = 0, action = -1) : Answer %.1f, Output %.1f'%(0, rl.getQ(0, -1)))
print('Q-value for (state = 0, action =  1) : Answer %.1f, Output %.1f'%(0, rl.getQ(0, 1)))
print('Q-value for (state = 1, action = -1) : Answer %.1f, Output %.1f'%(0, rl.getQ(1, -1)))
print('Q-value for (state = 1, action =  1) : Answer %.1f, Output %.1f'%(1, rl.getQ(1, 1)))

rl.incorporateFeedback(2, -1, 1, 1)
print('Incorporate the feedback of (s=2, a=-1, r=1, s\'=1)')
print('Q-value for (state = 2, action = -1) : Answer %.1f, Output %.1f'%(1.9, rl.getQ(2, -1)))
print('Q-value for (state = 2, action =  1) : Answer %.1f, Output %.1f'%(0, rl.getQ(2, 1)))
'''

############################################################

# Problem E: convergence of Q-learning

def compareQLandVI(targetMDP, featureExtractor):
    QL = QLearningAlgorithm(targetMDP.actions, 1, featureExtractor)
    VI = ValueIteration()
    
    util.simulate(targetMDP, QL, numTrials=30000)
    VI.solve(targetMDP)

    diffPolicyStates = []
    QL.explorationProb = 0
    for state in targetMDP.states:
        #print state, QL.getAction(state), VI.pi[state]
        if QL.getAction(state) != VI.pi[state]:
            diffPolicyStates.append(state)
    print("%d/%d = %f%% different states"%(len(diffPolicyStates), len(targetMDP.states), len(diffPolicyStates)/float(len(targetMDP.states))))

"""
print('\n========== Problem E ==========')
# Small test case
smallMDP = BlackjackMDP(cardValues=[1, 5], multiplicity=2, threshold=10, peekCost=1)
compareQLandVI(smallMDP, identityFeatureExtractor)

# Large test case
largeMDP = BlackjackMDP(cardValues=[1, 3, 5, 8, 10], multiplicity=3, threshold=40, peekCost=1)
compareQLandVI(largeMDP, identityFeatureExtractor)
"""

############################################################

# Problem F: features for Q-learning.

# You should return a list of (feature key, feature value) pairs (see
# identityFeatureExtractor()).
# Implement the following features:
# - indicator on the total and the action (1 feature).
# - indicator on the presence/absence of each card and the action (1 feature).
#       Example: if the deck is (3, 4, 0 , 2), then your indicator on the presence of each card is (1,1,0,1)
#       Only add this feature if the deck != None
# - indicator on the number of cards for each card type and the action (len(counts) features).  Only add these features if the deck != None
def blackjackFeatureExtractor(state, action):
    total, nextCard, counts = state
    # BEGIN_YOUR_CODE (our solution is 9 lines of code, but don't worry if you deviate from this)
    raise Exception("Not implemented yet")
    # END_YOUR_CODE

"""
print('\n========== Problem F ==========')

mdp = BlackjackMDP(cardValues=[1, 5], multiplicity=2, threshold=10, peekCost=1)
rl = QLearningAlgorithm(mdp.actions, mdp.discount(), blackjackFeatureExtractor, 0)

# We call this here so that the stepSize will be 1
rl.numIters = 1

rl.incorporateFeedback((7, None, (0, 1)), 'Quit', 7, (7, None, None))
print("Incorporate the feedback of (s=(7, None, (0, 1)), a='Quit', r=7, s'=(7, None, None))")
print("Q-value for (state = (7, None, (0, 1)), action = 'Quit') : Answer %.1f, Output %.1f"%(28, rl.getQ((7, None, (0, 1)), 'Quit')))
print("Q-value for (state = (7, None, (1, 0)), action = 'Quit') : Answer %.1f, Output %.1f"%(7, rl.getQ((7, None, (1, 0)), 'Quit')))
print("Q-value for (state = (2, None, (0, 2)), action = 'Quit') : Answer %.1f, Output %.1f"%(14, rl.getQ((2, None, (0, 2)), 'Quit')))
print("Q-value for (state = (2, None, (0, 2)), action = 'Take') : Answer %.1f, Output %.1f"%(0, rl.getQ((2, None, (0, 2)), 'Take')))

# Large test case
largeMDP = BlackjackMDP(cardValues=[1, 3, 5, 8, 10], multiplicity=3, threshold=40, peekCost=1)
compareQLandVI(largeMDP, blackjackFeatureExtractor)
"""

############################################################

