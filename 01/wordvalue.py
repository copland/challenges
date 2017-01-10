from data import DICTIONARY, LETTER_SCORES
from multiprocessing import Pool

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as f:
        content = f.read()
        return content.split('\n')[:-1]

def _is_valid_char(char):
    return True if LETTER_SCORES.get(char.upper(), None) else False 

def _accumulate_score(acc, nxt):
    return acc+LETTER_SCORES[nxt.upper()] if _is_valid_char(nxt) else acc

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return reduce(_accumulate_score , word, 0) 

def max_word_value(words=None):
    if not words:
        words = load_words()
    p = Pool(10)
    scores = p.map(calc_word_value, words)
    max_score = 0
    max_index = -1
    for i, score in enumerate(scores):
        if score > max_score:
            max_score = score
            max_index = i
    return words[max_index]
    
if __name__ == "__main__":
    max_word_value() 
     
