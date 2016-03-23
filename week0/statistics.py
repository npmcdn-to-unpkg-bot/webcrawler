import string
with open('Walden.txt', encoding='utf-8') as book:
    words = [raw_word.strip(string.punctuation).lower() for raw_word in book.read().split()]
    words_index = set(words)
    counts_dict = {index: words.count(index) for index in words_index}

for word in sorted(counts_dict, key=lambda x: counts_dict[x], reverse=True):
    print('{}-{}'.format(word, counts_dict[word]))
