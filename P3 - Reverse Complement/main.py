complements = {
    "A" : "T",
    "T" : "A",
    "C" : "G",
    "G" : "C"
}

with open("input.txt", "r") as f:
    text = f.readline().strip()

def reverseComplement(text):
    complement = "".join(map(complements.get, text))
    return complement[::-1]
    

with open("output.txt", "w") as f:
    f.write(reverseComplement(text))

