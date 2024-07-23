#onhot encoding
#calculate loss(nll)
#backpropagate
#update
import torch

words =  open('names.txt', 'r').read().split('\n')

char_list = sorted(set(''.join(words)))
stoi = {char: i+1 for i, char in enumerate(char_list)}
stoi['.'] = 0
itos =  {i: char for char, i in stoi.items()}

xs, ys = [], []

for word in words[:1]:
    word =  ['.'] + list(word) + ['.']
    for ch1, ch2 in zip(word, word[1:]): 
        x = stoi[ch1]
        y = stoi[ch2]
        xs.append(x)
        ys.append(y)
xs = torch.tensor(xs)
ys = torch.tensor(ys)        
print(xs)
print(ys)