
with open('5-grams.csv','r') as f:
    words = f.readlines()
wordlist = [l.rstrip('\n') for l in words]
#print(wordlist)


TRIES = 6
WORDLE = 'scare'

voc = dict(zip('abcdefghijklmnopqrstuvwxyz',[]))


def check(word, wordle):
    assert len(word) == 5, 'word should be of length 5'
    assert word in wordlist, 'word not in list'
    
    result = []
    for i, c in enumerate(word):
        if c in wordle:
            if word[i] == wordle[i]:
                res = 'HIT'
            else:
                res = 'INC'
        else:
            res = 'MIS'

        result.append({i: res})
    return result


print(check('beard','their'))

    
    
