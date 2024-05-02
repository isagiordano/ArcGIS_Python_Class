# 3. Given a singe phrase, count the occurrence of each word
# Using this string:

string = 'hi dee hi how are you mr dee'
# Count the occurrence of each word, and print the word plus the count
# (hint, you might want to "split" this into a list by a white space: " ").
# # Step 1. use string split function to split string into words

words_split = string.split()

# # create empty dictionary of word counts. will save each word as a key and as a word count value

word_counts = {}

# # for - makes a loop that goes over each word in the list word_split
# # if word in word counts - checks if each word is saved as a key in empty dictionary
# # word_counts[word] += 1 means if the word is not yet in word_counts dictionary, it gets a value of one,
# # and if it is already in the dictionary, it increases its value by one
# # else means if the word is not in the dictionary, it is added with value of one

for word in words_split:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# # print dictionary
print(word_counts)

# !! referenced from my friend Cassidy (a computer science major) who helped me understand all of these commands,
# and a little bit from
# https://www.geeksforgeeks.org/find-frequency-of-each-word-in-a-string-in-python/
