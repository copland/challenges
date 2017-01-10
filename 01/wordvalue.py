from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as f:
        return [word.strip('\n') for word in f.readlines()]

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    for letter in word:
        if letter.upper() in LETTER_SCORES.keys(): #should we disqualify words with bad characters?
            score += LETTER_SCORES[letter.upper()]
    return score
    
def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY
    """
    if not words:
        words = load_words()
    max_score = 0
    best_word = '' 
    for word in words:
        word_score = calc_word_value(word)
        if word_score > max_score:
            max_score = word_score
            best_word = word
    return best_word 
        

if __name__ == "__main__":
    pass # run unittests to validate
