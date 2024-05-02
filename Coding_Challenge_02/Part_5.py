# 5. User input 2
# Using the following dictionary (or a similar one you found on the internet), ask the user for a word,
# and compute the Scrabble word score for that word (Scrabble is a word game, where players make words
# from letters, e+ach letter is worth a point value), steal this code from the internet, format it and
# make it work:

letter_scores = { 'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4,
    'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3,
    'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8,
    'y': 4, 'z': 10
}

# # ask for input word
word = input("Scrabble word: ")

def scrabble_score(word):
    # defines scrabble score from the word input
    return sum(letter_scores[letter] for letter in word)
    #letter scores [letter] goes over every letter in the word and finds corresponding scrabble value
    # then return saves it and sum adds it up 
print("Scrabble score is " + str(scrabble_score(word)))

# !! referenced from
# https://stackoverflow.com/questions/32235033/creating-a-python-scrabble-function-that-takes-a-string-as-input-and-returns-a-s


