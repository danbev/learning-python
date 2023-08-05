import urllib
import requests
import pprint
import torch
import matplotlib.pyplot as plt

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
#pprint.pprint(sorted_embeddings)

N = torch.zeros((27, 27), dtype=torch.int32)

all_letters = ''.join(words)
chars = set(all_letters)
chars = sorted(list(set(all_letters)))
print(f'nr of unique_letters: {len(chars)}')
print(chars)

stoi = {ch: i+1 for i, ch in enumerate(chars)}
stoi['.'] = 0
itos = {i: ch for ch, i in stoi.items()}

for w in words:
  chs = ['.'] + list(w) + ['.']
  for ch1, ch2 in zip(chs, chs[1:]):
    ix1 = stoi[ch1]
    ix2 = stoi[ch2]
    N[ix1, ix2] += 1

#plt.imshow(N)
#plt.show()


plt.figure(figsize=(16,16), dpi=80)
plt.imshow(N, cmap='Blues')
for i in range(27):
    for j in range(27):
        chstr = itos[i] + itos[j]
        plt.text(j, i, chstr, ha="center", va="bottom", color='gray')
        plt.text(j, i, N[i, j].item(), ha="center", va="top", color='gray')
plt.axis('off');
#plt.show()

print(f'An entry in N is a Tensor: {type(N[2,2])}')
print(f'Use .item() to get the value: {N[2,2].item()}')
p = N[0]
print(f'convert from integers: {p}')
p = N[0].float()
p = p / p.sum()
print(f'to floats: {p}')
print(p.sum())
print(p.shape)

g = torch.Generator().manual_seed(18)
#p = torch.rand(3, generator=g)
#p = p / p.sum()
# So we are now going to take a stab at generating a characters and we do this
# by sampling from a multinomial distribution.
idx = torch.multinomial(p, num_samples=1, replacement=True, generator=g).item()
print(f'sampled index: {idx}')
sampled_char = itos[idx]
print(f'sampled character: {sampled_char}')
# So in this case we sampled the character 'j' from the distribution p.
print(f'Number of words starting with {sampled_char}: {N[0][idx]} (out of {N[0].sum()})')
# These words are the ones starting with '.j' in the matplot lib figure.
# So j is the first character in the word, and then we "move" to the row with
# row 'j.' to get the characters that are preceded by j.
print(f'Row for .{sampled_char}: {N[idx].tolist()} , max:{N[idx].max()}')
# Now we want to sample from this row for the next character which will follow
# the character 'j' in the word that starts with 'j'.
#
for i in range(20):
    output = []
    idx = 0
    while True:
        p = N[idx].float()
        p = p / p.sum()
        # We can verify that the model is actually trained despite the output
        # being mostly gibberish and not looking like real names.
        #p = torch.ones(27)/27.0 # untrained model
        idx = torch.multinomial(p, num_samples=1, replacement=True, generator=g).item()
        output.append(itos[idx])
        if idx == 0:
            break
    print(f"Generated: {''.join(output)}")
