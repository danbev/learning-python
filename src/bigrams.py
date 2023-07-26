import urllib
import requests
import pprint

"""
words = urllib.request.urlopen('https://raw.githubusercontent.com/karpathy/makemore/master/names.txt'
    ).read().decode('utf-8').splitlines()

# write words to file named names.txt
with open('names.txt', 'w') as f:
    for word in words:
        f.write(word + '\n')
"""

words = open('names.txt', 'r').read().splitlines()
print(words[:10])
print(len(words))
print(min(len(w) for w in words))
print(max(len(w) for w in words))


b = {}
for w in words:
  chs = ['<S>'] + list(w) + ['<E>']
  for ch1, ch2 in zip(chs, chs[1:]):
    bigram = (ch1, ch2)
    b[bigram] = b.get(bigram, 0) + 1

sorted_embeddings = sorted(b.items(), key = lambda kv: -kv[1])
pprint.pprint(sorted_embeddings)
