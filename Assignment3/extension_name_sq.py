"""
File: name_sq.py (extension)
Name:  Kang
----------------------------
This program is an extension of assignment3!
It will ask the user to provide a name, 
and the square pattern of the given name 
will be printed on the console.
"""


def main():
    print('This program prints a name in a square pattern!')
    name = str(input('Name: '))
    print(name)
    for i in range(len(name)-2):
        print(name[i+1], end='')
        print(' '*(len(name)-2), end='')
        print(name[-(i+2)])
    print(reverse_name(name))


def reverse_name(name):
    reverse = ''
    for i in range(len(name)-1, -1, -1):
        reverse += name[i]

    return reverse


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
