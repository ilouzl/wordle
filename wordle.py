
with open('5-grams.csv','r') as f:
    words = f.readlines()
wordlist = [l.rstrip('\n') for l in words]
#print(wordlist)


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

        result.append((c,res))
    return result, word == wordle


def guess(voc):
    return 'their'

def game(wordle, tries):
    
    voc = dict(zip('abcdefghijklmnopqrstuvwxyz',['NA']*22))
    print(voc)    
    while tries:
        print("tries ", tries)
        g = guess(voc)
        print(g)
        result, wordle_hit = check(g, wordle)
        if wordle_hit:
            print("YOU WON!!")
            return
        
        print(result)
        for c, r  in result:
            print(c,r)
            if voc[c] == 'NA':
                voc[c] = r

        print(voc)

        tries -= 1

        
game('beard',3)  
