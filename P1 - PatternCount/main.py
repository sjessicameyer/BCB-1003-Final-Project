

with open("input.txt", "r") as f:
    text = f.readline().strip()
    pattern = f.readline().strip()

def patternCount(text, pattern):
    count = 0
    for i in range(0, len(text)-len(pattern)):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count

with open("output.txt", "w") as f:
    f.write(str(patternCount(text, pattern)))

