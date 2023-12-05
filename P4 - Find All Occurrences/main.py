

with open("input.txt", "r") as f:
    pattern = f.readline().strip()
    text = f.readline().strip()

def allOccurences(pattern, text):
    occurences = []
    for i in range(0, len(text)-len(pattern)):
        if text[i:i+len(pattern)] == pattern:
            occurences.append(i)
    return occurences
    

with open("output.txt", "w") as f:
    f.write(" ".join(map(str, allOccurences(pattern, text))))

