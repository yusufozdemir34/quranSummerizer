from gensim.summarization import summarize
from gensim.summarization import keywords

file_text = open("bakara.txt")

text=file_text.read()
summary = summarize(text,word_count=100)
key_words = keywords(text,ratio=0.05)
print(key_words)
print(summary)