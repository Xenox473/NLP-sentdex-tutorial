# PART 1 : Sentence and word tokenizing

# import nltk

# nltk.download()

# tokenizing - word tokenizers and sentence tokenizers
# lexicon and corporas
# corpora - body of text
# lexicon - words and their means

from nltk.tokenize import sent_tokenize, word_tokenize

example_text = "Hello there, how are you doing today? The weather is great. Indeed it is. I am doing well."

print(sent_tokenize(example_text))
print(word_tokenize(example_text))

#  PART 2 : Stop Words

from nltk.corpus import stopwords

example_sentence = "This is an example showing off stop word filtration"
stop_words = set(stopwords.words("english"))

words = word_tokenize(example_sentence)
filtered_sentence = []
for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)
print (filtered_sentence)

# PART 3: Stemming

from nltk.stem import PorterStemmer

ps = PorterStemmer()
example_words = ["python", "pythoner", "pythoning", "pythoned", "pythonly"]
for w in example_words:
    print(ps.stem(w))
