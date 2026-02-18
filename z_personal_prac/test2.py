

from itertools import permutations
from PyDictionary import PyDictionary

from nltk.corpus import words

word_list = words.words()

combination_list = []

inputstr = 'appel'#.upper()#input("enter ")#.upper() #sys.argv[1].upper()
k = 5
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

print(combination_list)

# def searcher(words,dic_words):
#     for word in words:
#         if word in dic_words:
#             #if word == d_word:
#             print("word matched"+word)
#         # else:
#         #     return "word do not match"
# searcher(combination_list,word_list)