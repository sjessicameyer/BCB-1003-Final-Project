
with open("input.txt", "r") as f:
    text1 = f.readline().strip()
    text2 = f.readline().strip()

def hammingDistance(text1, text2):
    distance = 0
    for i in range(0, len(text1)):
        if text1[i] != text2[i]:
            distance += 1
    return distance

with open("output.txt", "w") as f:
    f.write(str(hammingDistance(text1, text2)))

