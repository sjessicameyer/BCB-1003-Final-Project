import collections
import functools
complements = {
    "A" : "T",
    "T" : "A",
    "C" : "G",
    "G" : "C"
}
bases = complements.keys()

with open("input.txt", "r") as f:
    text = f.readline().strip()
    k, d = map(int, f.readline().split(" "))

def reverseComplement(text):
    complement = "".join(map(complements.get, text))
    return complement[::-1]

#returns a list of all kmers within a hamming distance of d
def withinDistance(kmer, d):
    def withinDistance(kmer, d, index):
        if d < 1 or index >= len(kmer):
            return [kmer]
        else:
            kmers = []
            #recursion hell, sorry
            for b in bases: 
                if b != kmer[index]:
                    kmers.append(kmer[:index] + b + kmer[index + 1:])
            return functools.reduce(lambda x, y: x+y, [withinDistance(k, d - 1, index + 1) for k in kmers] + [withinDistance(kmer, d, index + 1)])
    return withinDistance(kmer, d, 0)


#returns the most frequent kmer within a hamming distance of d
#in text with a length of k
def mostFrequent(text, k, d):
    kmers = collections.defaultdict(int)
    for t in [text, reverseComplement(text)]:
        for i in range(0, len(t)-k+1): 
            substr = t[i:i+k]
            for kmer in withinDistance(substr, d):
                kmers[kmer] += 1
    max_freq = max(kmers.values())
    return [key for key in kmers.keys() if kmers[key] == max_freq]


with open("output.txt", "w") as f:
    f.write(" ".join(mostFrequent(text, k, d)))