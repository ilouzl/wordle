
with open('5-grams.csv','r') as f:
    words = f.readlines()
wordlist = [l.rstrip('\n') for l in words]

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


def update_wordlist(wordlist, voc):
    for c, v in voc.items():
        if v[0] == 'HIT':
            wordlist = [w for w in wordlist if w[v[1]] == c]
        if v[0] == 'MIS':
            wordlist = [w for w in wordlist if c not in w]
        if v[0] == 'INC':
            for i in v[1:]:
                wordlist = [w for w in wordlist if c in w and w[i] != c]
    return wordlist

def game(wordle, tries, wordlist): 
    voc = {k: ['NA'] for k in 'abcdefghijklmnopqrstuvwxyz'}
    for t in range(tries):
        print("try ", t + 1)
        wordlist = update_wordlist(wordlist, voc)
        guess = wordlist[0]
        print("Guess - \"%s\""%(guess))
        result, wordle_hit = check(guess, wordle)
        if wordle_hit:
            print("YOU WON!!")
            return
        
        print(result)
        for i, res  in enumerate(result):
            c, r = res
            if r == 'HIT':
                voc[c] = [r, i]
            elif r == 'INC':
                if voc[c][0] != 'HIT':
                    voc[c][0] = r
                    voc[c].append(i)
            else:
                voc[c] = ['MIS']

if __name__ == '__main__':
    import sys
    wordle, tries = sys.argv[1], int(sys.argv[2])
    game(wordle, tries, wordlist)  
