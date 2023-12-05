

with open("input.txt", "r") as f:
    pattern = f.readline().strip()
    text = f.readline().strip()

def allOccurrences(pattern, text):
    occurrences = []
    for i in range(0, len(text)-len(pattern)):
        if text[i:i+len(pattern)] == pattern:
            occurrences.append(i)
    return occurrences
    

with open("output.txt", "w") as f:
    f.write(" ".join(map(str, allOccurrences(pattern, text))))

