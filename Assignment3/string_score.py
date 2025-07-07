"""
File: string_score.py
Name: Kang
------------------------------
This program calculates a score for a given string based on 
the types of characters it contains. It assigns points as follows: 
digits are worth 1 point, uppercase letters are worth 2 points, 
and lowercase letters are worth 3 points. The score() function 
goes through each character in the string, adds up the points 
according to its type, and then prints out the total score.
"""


def main():
    score('1aB4rC')    # digit->1 ; upper->2; lower->3
    # 12
    score('aaaaA3')
    # 15


def score(string):
    total = 0
    for i in range(len(string)):
        if string[i].isdigit():
            total += 1
        elif string[i].isupper():
            total += 2
        else:
            total += 3
    print(total)



if __name__ == '__main__':
    main()