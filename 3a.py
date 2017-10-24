def longest_word(text):
    with open(text, 'r') as infile:
        words = infile.read().split()
    max_len = len(max(words, key=len))
            return [word for word in words if len(word) == max_len] #one line comprehention

print(longest_word('text.txt'))
