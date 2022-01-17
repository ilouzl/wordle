
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
    
    voc = {k: ['NA'] for k in 'abcdefghijklmnopqrstuvwxyz'}
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
        for i, res  in enumerate(result):
            c, r = res
            print(i,c,r)
            if r == 'HIT':
                voc[c] = [r, i]
            elif r == 'INC':
                if voc[c][0] != 'HIT':
                    voc[c][0] = r
                    voc[c].append(i)
            else:
                voc[c] = ['MIS']

        print(voc)

        tries -= 1

        
game('beard',1)  
