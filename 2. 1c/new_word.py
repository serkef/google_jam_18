from itertools import product

results = []
response = "Case #{x}: {y}"


def find_word(words, word_length, nof_words):
    word_wh = {word: True for word in words}

    letter_wh = {idx: set(w[idx] for w in words) for idx in range(word_length)}

    for word in (''.join(comb) for comb in product(*letter_wh.values())):
        if word not in word_wh:
            return word
    else:
        return '-'


for case in range(int(input(''))):
    nof_words, word_length = map(int, (input('')).split())
    words = []

    for _ in range(nof_words):
        words.append(input(''))

    word = find_word(words, word_length, nof_words)
    results.append(response.format(x=case + 1, y=word))

for result in results:
    print(result)