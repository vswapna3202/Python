# This program given a list of N items and its prices that consumers bought from a 
# supermarket on a particular day prints each item and its price in order of its first
# occurence.
# Input:   First line has input of N - number of items
#          Next lines has input of N items with item_name item_price 
#          where item_name is name of item purchased
#                item_price is price of item purchased
# Output:  
#          item_name net_price (Quantity * item_price)
# Import relevant libraries
from collections import OrderedDict
# Input number of items
N = int(input())
# Create store dictionary Ordered Dictionary object
store_dictionary = OrderedDict()
# Loop through each item and obtain name of item and its price
# Store item_price if item is entered first time and add to 
# existing item_price for subsequent re-entries
for _ in range(N):
    item = input().split()
    item_name = " ".join(item[:-1])
    item_price = int(item[-1])
    if store_dictionary.get(item_name):
        store_dictionary[item_name] += item_price
    else:
        store_dictionary[item_name] = item_price
# Print the store item name and the prices
print()
for i in store_dictionary.keys():
    print(i, store_dictionary[i])