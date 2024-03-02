# This program accepts n number of words and prints the number of occurences for 
# each word.
# Input: The first line contains the integer, n
#        The next  lines each contain a word.
# Output: On the first line, output the number of distinct words from the input.
#         On the second line, output the number of occurrences for each distinct 
#         word according to their appearance in the input.
from collections import OrderedDict

n = int(input()) # Input number of words
words = []
word_count = OrderedDict()
for _ in range(n):  # Loop for all words
    words.extend(input().split()) # Split the words and add to words array

for word in words:      # For each word
    if word in word_count: # Check if word is in word_count ordered dictionary
        word_count[word] += 1 # If its a match increase count
    else:               
        word_count[word] = 1 # If not initialise to 1 as there is just 1 word

print(len(word_count))  # Print number of words which is length of word_count
# Loop through word_count values and print count for each word on same line
for count in word_count.values():
    print(count, end= " ")
