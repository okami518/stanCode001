"""
File: similarity.py (extension)
Name: Kang
----------------------------
This program is an extension of assignment3!
It will compare short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    # Get DNA sequences from user input
    long_sequence = str(input('Please give me a DNA sequence to search: ')).upper()
    short_sequence = str(input('What DNA sequence would you like to match? ')).upper()
    similar = -float('inf')  # Track highest similarity score
    homology = ''  # Store the best matching sequence

    # Slide through all possible subsequences in the long sequence
    for i in range(len(long_sequence)-len(short_sequence)+1):  # Number of slides = long - short
        score = 0
        update_string = ''
        compare_sequence = get_sequence(i, long_sequence, short_sequence)  # 得到比較的片段
        for j in range(len(short_sequence)):  # 因為是比短的片段，所以是len(short_sequence)
            if compare_sequence[j] == short_sequence[j]:
                score += 1
                update_string += compare_sequence[j]
            else:
                update_string += compare_sequence[j]

        # Update the best match if higher score found
        if score > similar:
            homology = update_string
    if similar == 0:
        print('There is no homology')
    else:
        print(f"The best match is {homology}")


def get_sequence(i, long_sequence, short_sequence):
    # Extract subsequence starting at index i.
    compare_sequence = long_sequence[i: i+(len(short_sequence))]
    return compare_sequence


if __name__ == '__main__':
    main()
