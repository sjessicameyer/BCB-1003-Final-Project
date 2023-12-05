import collections

with open("input.txt", "r") as f:
    text = f.readline().strip()
    k, L, t = map(int, f.readline().strip().split(" "))

#find all kmers of length k in text and their frequency
def allKmers(text, k):
    kmers = collections.defaultdict(int)
    for i in range(0, len(text)-k):
        substr = text[i:i+k]
        kmers[substr] += 1
    return kmers

#find all kmers of length k in text with at least frequency t
def allFrequentKmers(text, k, t):
    kmers = allKmers(text, k)
    return [key for key in kmers if kmers[key] >= t]

#find all kmers of length k in text that form clumps of length L with at least frequency t
def findKmersInClumps(text, k, L, t):
    kmers = set()
    for i in range(0, len(text)-L):
        kmers.update(allFrequentKmers(text, k, t))
    return kmers

with open("output.txt", "w") as f:
    f.write(" ".join(findKmersInClumps(text, k, L, t)))

