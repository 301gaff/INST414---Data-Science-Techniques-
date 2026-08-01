from collections import Counter
import string
from nltk.tokenize import TweetTokenizer

input_file_path = "test01_cc_sharealike.txt"

with open(input_file_path, "r", encoding="utf-8") as file:
    text = file.read()

tokenizer = TweetTokenizer()

tokens = tokenizer.tokenize(text.lower())

words = []

for token in tokens:
    if token not in string.punctuation:
        words.append(token)

word_counts = Counter(words)

for word, count in word_counts.most_common(10):
    print(f"{word}\t{count}")
-----------------------------------------------------------------------
from collections import Counter
import string
from nltk.tokenize import TweetTokenizer

input_file_path = "test02_the_last_question.txt"

with open(input_file_path, "r", encoding="utf-8") as file:
    text = file.read()

tokenizer = TweetTokenizer()

tokens = tokenizer.tokenize(text.lower())

words = []

for token in tokens:
    if token not in string.punctuation:
        words.append(token)

word_counts = Counter(words)

for word, count in word_counts.most_common(10):
    print(f"{word}\t{count}")
