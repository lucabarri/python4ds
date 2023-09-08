import string

# NOTE: the string package is needed for
#       accessing punctuation characters.
#       Next we print these,
print("We're removing the following characters")
print(string.punctuation)

# Reades data
with open('./data/shakespeare.txt', 'r') as f:
    data = f.read()

# Converts line breaks into empty spaces
data = data.replace('\n', ' ').lower()

# splits data into
tokens = data.split(' ')

# Removes trailing whitespaces from tokens
tokens = [t.strip() for t in tokens if t not in string.punctuation]

# Gets the unique tokens
unique_tokens = list(set(tokens))

# Calculates frequencies of tokens
frequencies = [tokens.count(t) for t in unique_tokens]

# Calculating indices for least frequent words
indices_least_frequent = [
    x for x, _ in sorted(enumerate(frequencies),
                         key=lambda x: x[1])
]

# Inverting the list
indices_most_frequent = indices_least_frequent[::-1]

# Prints tokens and frequencies
for i in indices_most_frequent[:30]:
    print(f"Token: {unique_tokens[i]}\tFrequency: {frequencies[i]}")
