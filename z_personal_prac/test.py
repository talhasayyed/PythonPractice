# random word match dictionary


import sys
from itertools import permutations
from PyDictionary import PyDictionary
import nltk
from nltk.corpus import words




# nltk.download()

#
#
#
# inputstr = 'fcuk'.upper()#input("enter ")#.upper() #sys.argv[1].upper()
# k = 4
#
# def word_combination(word_str,lenght):
#     if k <= len(inputstr):
#         lst_inp = list(inputstr)
#
#         perms = (p for p in permutations(lst_inp,k))
#
#
#         for p in perms:
#             word = ''.join(p)
#             print(word)
#         #     for word_ in word_list:
#         #         if word_ == word:
#         #             yield (word_ + "<--word  matches")
#         #     else:
#         #         yield " not found"
#             # print(word)
#
#
#             # for wrd in word_list:
#             #     print(wrd)
#                 # if wrd == word:
#                 #     print(word)
#
#     # else:
#     #     print('u have inserted high number')
#
# word_combination(inputstr,k)


#
# print(v.__next__())

# -----------Dict stuff

# word = "about"
# dictionary = PyDictionary(word)
# meaning = dictionary.printMeanings()
# print(f'word is {word} \nmeaning is {meaning}')



wrd_lst = ['APPEL', 'APPLE', 'APEPL', 'APELP', 'APLPE', 'APLEP', 'APPEL', 'APPLE', 'APEPL', 'APELP', 'APLPE', 'APLEP', 'AEPPL', 'AEPLP', 'AEPPL', 'AEPLP', 'AELPP', 'AELPP', 'ALPPE', 'ALPEP', 'ALPPE', 'ALPEP', 'ALEPP', 'ALEPP', 'PAPEL', 'PAPLE', 'PAEPL', 'PAELP', 'PALPE', 'PALEP', 'PPAEL', 'PPALE', 'PPEAL', 'PPELA', 'PPLAE', 'PPLEA', 'PEAPL', 'PEALP', 'PEPAL', 'PEPLA', 'PELAP', 'PELPA', 'PLAPE', 'PLAEP', 'PLPAE', 'PLPEA', 'PLEAP', 'PLEPA', 'PAPEL', 'PAPLE', 'PAEPL', 'PAELP', 'PALPE', 'PALEP', 'PPAEL', 'PPALE', 'PPEAL', 'PPELA', 'PPLAE', 'PPLEA', 'PEAPL', 'PEALP', 'PEPAL', 'PEPLA', 'PELAP', 'PELPA', 'PLAPE', 'PLAEP', 'PLPAE', 'PLPEA', 'PLEAP', 'PLEPA', 'EAPPL', 'EAPLP', 'EAPPL', 'EAPLP', 'EALPP', 'EALPP', 'EPAPL', 'EPALP', 'EPPAL', 'EPPLA', 'EPLAP', 'EPLPA', 'EPAPL', 'EPALP', 'EPPAL', 'EPPLA', 'EPLAP', 'EPLPA', 'ELAPP', 'ELAPP', 'ELPAP', 'ELPPA', 'ELPAP', 'ELPPA', 'LAPPE', 'LAPEP', 'LAPPE', 'LAPEP', 'LAEPP', 'LAEPP', 'LPAPE', 'LPAEP', 'LPPAE', 'LPPEA', 'LPEAP', 'LPEPA', 'LPAPE', 'LPAEP', 'LPPAE', 'LPPEA', 'LPEAP', 'LPEPA', 'LEAPP', 'LEAPP', 'LEPAP', 'LEPPA', 'LEPAP', 'LEPPA']

# wrd_lst = 'fuck'


word_list = words.words()

def WordDic(inp):
    for wr in wrd_lst:

        if wr in word_list:
            print(f"{wr} present ")

    else:
        print('not present')

WordDic(wrd_lst)
