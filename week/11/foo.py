

def convert(word):

    twoLetterGraphemes=["ch"]
    oneLetterGraphemes=["b","D","a","q", "'", "H", "p", "l"]

    sounds={"b" : "b",
            "ch": "t͡ʃ",
            "D" : "ɖ",
            "a" : "ɑ",
            "q" : "qʰ",
            "'" : "ʔ",
            "p" : "pʰ",
            "H" : "x",
            "l" : "l"
           }

    
    start=0
    end=len(word)

    result = ""

    while start < end:
        
        if word[start:start+2] in twoLetterGraphemes:
            result += sounds[word[start:start+2]]
            start += 2

        else:
            result += sounds[word[start:start+1]]
            start += 1

    return result



def reduplicate(noun):
    return noun + "-" + noun
    

