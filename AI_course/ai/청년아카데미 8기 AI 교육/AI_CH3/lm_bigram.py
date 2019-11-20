import math, collections


SENTENCE_BEGIN = '-BEGIN-' # 문장의 맨 앞을 의미함

corpus = [
    'I am Sam',
    'Sam I am',
    'I do not like green'
]
    
# Counting
unigram_counts = collections.defaultdict(int)
for sentence in corpus:
    words = [SENTENCE_BEGIN] + sentence.split()
    for word in words:
        unigram_counts[word] += 1

bigram_counts = collections.defaultdict(int)
for sentence in corpus:
    words = [SENTENCE_BEGIN] + sentence.split()
    for i in range(len(words)-1):
        bigram_counts[(words[i], words[i+1])] += 1 # key : pair of (words[i], words[i+1]), value : count of (words[i],words[i+1])
        
# Bigram function
def bigram(prev_word, curr_word):
    return float(bigram_counts[(prev_word, curr_word)]) / unigram_counts[prev_word]

# Printing results
print('\n- Bigram probabilities - ')
print(('P(-BEGIN-, I) = %f'%bigram(SENTENCE_BEGIN, 'I')))    
print(('P(-BEGIN-, Sam) = %f'%bigram(SENTENCE_BEGIN, 'Sam')))    
print(('P(I, do) = %f'%bigram('I', 'do')))
print(('P(like, green) = %f'%bigram('like', 'green')))  # output = 1의 의미는 100% 확률로 'like' 다음에 'green'이 나온다는 의미.
