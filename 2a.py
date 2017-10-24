from collections import Counter
def word_count(text):
    with open(text) as f: 
        print Counter(f.read().split())

word_count("text.txt")
