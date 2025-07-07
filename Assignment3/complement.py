"""
File: complement.py
Name: Kang
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():

    print(dict_build_complement('ATC'))
    print(dict_build_complement(''))
    print(dict_build_complement('ATGCAT'))
    print(dict_build_complement('GCTATAC'))


def build_complement(dna):
    my_dna = ''
    if dna == '':
        print('DNA strand is missing', end='')
    else:
        for i in range(len(dna)):
            if dna[i] == 'A':
                my_dna += 'T'
            elif dna[i] == 'T':
                my_dna += 'A'
            elif dna[i] == 'C':
                my_dna += 'G'
            elif dna[i] == 'G':
                my_dna += 'C'
    return my_dna


def dict_build_complement(dna):
    my_dna = ''
    dic = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    if dna == '':
        print('DNA strand is missing', end='')
    else:
        for i in range(len(dna)):
            my_dna += dic[dna[i]]
    return my_dna






# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
