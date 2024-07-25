import re

def LongestWord(sen):
    sen = re.sub(r'[^a-zA-Z0-9\s]', '', sen)
    words = sen.split()
    return max(words, key=len)


# keep this function call here 
print(LongestWord(input()))
