from nltk.corpus import words
from itertools import permutations


word_list = words.words()

combination_list = []

inputstr = input("Enter Alphabets: ")#.upper() #sys.argv[1].upper()

k = int(input("Enter Alphabet lengths: "))
# will create comb_word list
def word_combination(word_str, lenght):
    if k <= len(inputstr):
        lst_inp = list(inputstr)

        # create permutation of every alphobet
        perms = (p for p in permutations(lst_inp, k))
        # print(type(perms))

        # iterating through every perms iterable and join to str fromat and append to
        for p in perms:
            word = ''.join(p)
            #print(word)
            combination_list.append(word)

word_combination(inputstr, k)

#print(combination_list)


word_list = words.words()

def WordDic(inp):
    for wrd in combination_list:
        if wrd in word_list:
            print(f"{wrd} present ")
    print('....end ...')


WordDic(combination_list)








