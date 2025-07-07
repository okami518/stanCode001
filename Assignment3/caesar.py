"""
File: caesar.py
Name: Kang
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    # Run the decryption functions
    # decipher()  # Simple version (commented out)
    decipher_dic()


def decipher():
    # Decrypt using shifted alphabet (simple method)
    shift = int(input('Secret number: '))
    my_alphabet = ALPHABET[-shift:]+ALPHABET[0:-shift]
    cipher = str(input("What's the ciphered string? ")).upper()
    deciphered = ''

    for ch in cipher:
        if ch.isalpha():
            index = my_alphabet.find(ch)
            deciphered += ALPHABET[index]
        else:
            deciphered += ch

    print(f"The deciphered string is: {deciphered}")


def decipher_dic():
    # Decrypt using a dictionary for better efficiency
    shift = int(input('Secret number: '))
    dic = my_alphabet_dic(shift)
    cipher = str(input("What's the ciphered string? ")).upper()
    deciphered = ''

    for ch in cipher:
        if ch.isalpha():
            index = dic[ch]
            deciphered += ALPHABET[index]
        else:
            deciphered += ch

    print(f"The deciphered string is: {deciphered}")


def my_alphabet_dic(shift):
    # Create a dictionary to map ciphered letters back to original letters
    my_alphabet = ALPHABET[-shift:]+ALPHABET[0:-shift]
    dic = {}
    for i in range(len(my_alphabet)):
        dic[my_alphabet[i]] = i
    return dic


if __name__ == '__main__':
    main()
