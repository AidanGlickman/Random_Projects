import re

def seg(word, mapping):
    letters = ["", "", "", "", ""]
    for i in list(word):
        letter = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        val = mapping[i]

        if "1" in val:
            letter[0][1] = "="
        if "2" in val:
            letter[1][0] = "|"
        if "3" in val:
            letter[1][2] = "|"
        if "4" in val:
            letter[2][1] = "="
        if "5" in val:
            letter[3][0] = "|"
        if "6" in val:
            letter[3][2] = "|"
        if "7" in val:
            letter[4][1] = "="
        
        line = 0
        for i in letter:
            for j in i:
                letters[line] = letters[line] + j
            letters[line] = letters[line] + "   "
            line = line+1
    return "\n".join(letters)



def readList(file, term):
    with open(file, "r") as words:
        wordlist = words.read().split(term)
        return wordlist

def readMappings(file):
    mappings = {}
    with open(file, "r") as words:
        wordlist = words.read().split("\n")
        for line in wordlist:
            line = line.split(" ")
            mappings[line[0]] = line[1].split(",")
        return mappings

def search(wordlist, bad):
    
    wordlist.sort(key = lambda s: len(s), reverse=True)
    for i in wordlist:
        if not bad.findall(i):
            return i

def main():
    bad = re.compile(r"[gikmoqvwxz]")
    wordlist = readList("words_alpha.txt", "\n")
    mappings = readMappings("segmap.txt")
    longest = search(wordlist, bad)
    output = seg(longest.upper(), mappings)
    print(longest)
    print(output)

main()