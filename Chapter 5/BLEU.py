from nltk.translate.bleu_score import sentence_bleu
from nlt.translate.bleu_score import SmoothingFunction


# Example 1
reference = [['the', 'cat', 'like', 'milk'], ['cat', 'likes', 'milk']]
candidate = ['the', 'cat', 'likes', 'milk']
score = sentence_bleu(reference, candidate)
print('Example 1', score)


# Example 2
reference = [['the', 'cat', 'likes', 'milk']]
candidate = ['the', 'cat', 'likes', 'milk']
score = sentence_bleu(reference, candidate)
print('Example 2', score)

# EXample 3
reference = [['the', 'cat', 'likes', 'milk']]
candidate = ['the', 'cat', 'enjoys', 'milk']
score = sentence_bleu(reference, candidate)
print('Example 3', score)

# Example 4
reference = [['je','vous','invite', 'a', 'vous', 'lever','pour', 'cette', 'minute', 'de', 'silence']]
candidate = ['levez','vous','svp','pour', 'cette', 'minute', 'de', 'silence']
score = sentence_bleu(reference, candidate)
print('Example 4', score)

chencherry = SmoothingFunction()
r1 = list('je vous invite a vous lever pour cette minute de silence')
candidate = list('levez vous svp pour cette minute de silence')



print('with smoothing score', sentence_bleu([r1], candidte, smoothing_function=chencherry.method1))
