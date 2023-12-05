

with open("input.txt", "r") as f:
    pattern = f.readline().strip()
    text = f.readline().strip()
    d = int(f.readline())

def hammingDistance(text1, text2):
    distance = 0
    for i in range(0, len(text1)):
        if text1[i] != text2[i]:
            distance += 1
    return distance

def allApproxOccurences(pattern, text, d):
    occurences = []
    for i in range(0, len(text)-len(pattern)):
        if hammingDistance(pattern, text[i:i+len(pattern)]) <= d:
            occurences.append(i)
    return occurences
    

with open("output.txt", "w") as f:
    f.write(" ".join(map(str, allApproxOccurences(pattern, text, d))))

