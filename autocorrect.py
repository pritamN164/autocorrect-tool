from collections import Counter
import re
from textblob import TextBlob

# Load dataset
def load_words(file_path=r"C:\Users\prita\OneDrive\Desktop\pinnacle\autocorrect-tool\data\word.txt.txt"):
    with open(file_path, "r") as f:
        words = f.read().split()
    return words

WORDS = Counter(load_words())

# Probability of a word
def P(word, N=sum(WORDS.values())):
    return WORDS[word] / N if N > 0 else 0

# Generate correction
def correction(word):
    return max(candidates(word), key=P)

# Generate candidates
def candidates(word):
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

# Known words
def known(words_list):
    return set(w for w in words_list if w in WORDS)

# Edit distance 1
def edits1(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

# Edit distance 2
def edits2(word):
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

# Sentence correction
def correct_sentence(sentence):
    corrected_words = []
    for w in sentence.split():
        corrected_words.append(correction(w))
    return " ".join(corrected_words)

# Grammar correction
def grammar_correct(text):
    return str(TextBlob(text).correct())