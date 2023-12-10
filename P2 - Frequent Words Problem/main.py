import collections

with open("input.txt", "r") as f:
    text = f.readline().strip()
    k = int(f.readline())

def mostFrequent(text, k):
    #default value of 0 for all kmers
    kmer_count = collections.defaultdict(int)

    #increment kmer_count
    for i in range(0, len(text)-k+1):
        substr = text[i:i+k]
        kmer_count[substr] += 1

    #filter kmers by highest count
    highest_count = max(kmer_count.values()) 
    return [kmer for kmer, count in kmer_count.items() 
            if count == highest_count]

with open("output.txt", "w") as f:
    f.write(" ".join(mostFrequent(text, k)))