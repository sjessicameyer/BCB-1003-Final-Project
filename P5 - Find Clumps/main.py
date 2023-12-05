import collections

with open("input.txt", "r") as f:
    text = f.readline().strip()
    k, L, t = map(int, f.readline().strip().split(" "))


#Parses text into a dictionary. 
#Keys are k-length kmers, and values are a list of where those keys appear in text.
def kmerLocations(text, k):
    occurences = collections.defaultdict(list)
    for i in range(0, len(text)-k):
        substr = text[i:i+k]
        occurences[substr].append(i)
    return occurences

#find if clump of length L with occurences t occurs based on locations, a list of indexes
def doesClumpExist(locations, L, t):
    for i in range(0, len(locations)-t+1):
        if (locations[i+t-1] - locations[i]) < L:
            return True
    return False

#find all kmers of length k in text that form clumps of length L with at least frequency t
def findKmersInClumps(text, k, L, t):
    kmers_in_clumps = set()
    for kmer, locations in kmerLocations(text, k).items():
        if doesClumpExist(locations, L, t):
            kmers_in_clumps.add(kmer)
    return kmers_in_clumps

with open("output.txt", "w") as f:
    f.write(" ".join(findKmersInClumps(text, k, L, t)))

