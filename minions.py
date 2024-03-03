# This program helps Kevin and Stuart play the Minion Game. Both players are 
# given the same string S. Both players have to make substrings using the 
# letters of the string S. Stuart has to make words starting with consonants
# and Kevin has to make words starting with vowels. The game ends when both
# players have made all possible substrings. A player gets +1 score for each
# occurence of the substring in string S. The winner is decided based on the 
# final score.
# Input: A single line of input containing the string S.
# Note: The string  will contain only uppercase letters:[A - Z].
#       Vowels are [A,E,I,O,U]
# Output: Name of player score for winner player and their score
# This function accepts a string and prints the winner of the minion
# game depending on number of vowels and consonants starting substrings
# is formed.
def minion_game(string):
    s =  len(string)
    vowel_score = 0
    consonant_score = 0
    for i in range(s):
        if string[i] in "AEIOU":
            vowel_score += (s-i)
        else:
            consonant_score += (s-i)
    if vowel_score > consonant_score:
        print("Kevin",str(vowel_score))
    elif consonant_score > vowel_score:
        print("Stuart",str(consonant_score))
    else:
        print("Draw")

S = input().strip()
minion_game(S)
