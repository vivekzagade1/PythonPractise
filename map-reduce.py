from functools import reduce


def count_words(doc):
    normalized_doc = "".join(c.lower() if c.isalpha() else " " for c in doc)
    frequencies = {}
    for word in normalized_doc.split():
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies


count_words('it was a beautiful day. I was running')

document = [
            'it was a beautiful day. I was running',
            'it was a beautiful day. I was running',
            'it was a beautiful day. I was running'
]

counts = map(count_words, document)
print(counts)


def combine_counts(d1, d2):
    d = d1.copy()
    for word, count in d2.items():
        d[word] = d.get(word, 0) + count
    return d


total_counts = reduce(combine_counts, counts)
print(total_counts)
