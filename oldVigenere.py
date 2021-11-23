#!/usr/bin/python3

import sys
from collections import Counter

# taken from Wikipedia
letter_freqs = {
    'A': 0.08167,
    'B': 0.01492,
    'C': 0.02782,
    'D': 0.04253,
    'E': 0.12702,
    'F': 0.02228,
    'G': 0.02015,
    'H': 0.06094,
    'I': 0.06966,
    'J': 0.00153,
    'K': 0.00772,
    'L': 0.04025,
    'M': 0.02406,
    'N': 0.06749,
    'O': 0.07507,
    'P': 0.01929,
    'Q': 0.00095,
    'R': 0.05987,
    'S': 0.06327,
    'T': 0.09056,
    'U': 0.02758,
    'V': 0.00978,
    'W': 0.02361,
    'X': 0.00150,
    'Y': 0.01974,
    'Z': 0.00074
}

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def pop_var(s):
    """Calculate the population variance of letter frequencies in given string."""
    freqs = Counter(s)
    mean = sum(float(v)/len(s) for v in freqs.values())/len(freqs)
    return sum((float(freqs[c])/len(s)-mean)**2 for c in freqs)/len(freqs)


# Populating the graph to calculate the frequency of repetition in order to predict key length
# def pop_graph(s):
#     while i < len(s):


if __name__ == "__main__":
    # Read ciphertext from stdin
    # Ignore line breaks and spaces, convert to all upper case
    cipher = sys.stdin.read().replace("\n", "").replace(" ", "").upper()

    #################################################################
    # Your code to determine the key and decrypt the ciphertext here
    matrix = list()
    matrix.append(cipher)
    s = cipher
    comparison = list()
    for i in range(len(cipher)):
        s = ' ' + s
        s = s[:len(cipher)]
        matrix.append(s)

    repeats = list()

    for i in range(1, 100):
        counter = 0
        for j in range(len(cipher)):
            if cipher[j] == matrix[i][j]:
                counter = counter + 1
        repeats.append(counter)

    repMax = repeats[0]

    for i in range(len(repeats)):
        if repeats[i] > repMax:
            repMax = repeats[i]

    keyLen = repeats.index(repMax) + 1

    chunks = [cipher[i:i+keyLen] for i in range(0, len(cipher), keyLen)]

    myCaesar = list()

    for i in range(keyLen):
        tempStr = ''
        for j in range(len(chunks)-1):
            tempStr = tempStr + chunks[j][i]
        myCaesar.append(tempStr)

    occurMatrix = list()

    for i in range(len(myCaesar)):
        occurMatrix.append(sorted(Counter(myCaesar[i]).items()))

    maxOcc = list()

    for i in range(len(occurMatrix)):
        maxOcc.append(max(occurMatrix[i]))

    myChar = list()

    for i in range(len(maxOcc)):
        myChar.append((ord(maxOcc[i][0]) - 65 - 4))

    caesarKey = list()

    for i in range(len(myChar)):
        caesarKey.append(alphabet[myChar[i]])

    print(caesarKey)

    # Logan: Cracking Vigenere Cipher Steps.
    # Guess key length n

    # Step1: First make a nxn Matrix populating all of the possible combinations.
    # Step2: Compare and record the number of repetitions that exist in that row
    # Step3: Use this to find or estimate the length of the key
    # Step4: Once you have a potential len of the key, use this to divide the cyphertext into blocks in the len of key.
    # Step5: Apply the frequency to each index of key in the blocked cyphertext
    # Step6: Estimate the shift using the frequency data
    # Step7: Apply this multiple times to estimate the key
    # Step8: Test this key against your cyphertext to ensure that you have the right key
    # Step9: Print out the key for grading.
