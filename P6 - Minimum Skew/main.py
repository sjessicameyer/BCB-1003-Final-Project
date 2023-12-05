
with open("input.txt", "r") as f:
    text = f.readline().strip()

#returns a list representing skew for all indexes in text
def getSkew(text):
    skew = [0]
    for i in range(0, len(text)):
        if text[i] == "C":
            skew.append(skew[i] - 1)
        elif text[i] == "G":
            skew.append(skew[i] + 1)
        else:
            skew.append(skew[i])
    return skew


def minimumSkewPositions(text):
    skew = getSkew(text)
    min_skew = min(skew)
    return [i for i, val in enumerate(skew) if val == min_skew]


with open("output.txt", "w") as f:
    f.write(" ".join(map(str, minimumSkewPositions(text))))

