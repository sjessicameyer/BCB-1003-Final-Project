import collections

with open("input.txt", "r") as f:
    text = f.readline().strip()
    k = int(f.readline())

def mostFrequent(text, k):
    kmers = collections.defaultdict(int)
    for i in range(0, len(text)-k+1):
        substr = text[i:i+k]
        kmers[substr] += 1
    max_freq = max(kmers.values())
    return [key for key in kmers.keys() if kmers[key] == max_freq]

with open("output.txt", "w") as f:
    f.write(" ".join(mostFrequent(text, k)))