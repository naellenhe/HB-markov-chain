"""Generate Markov text from text files."""

import sys
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    text_file = open(file_path)
    text_string= text_file.read()
    text_file.close()
    return text_string


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    n = int(raw_input("Enter the number of ngrams you want? >"))
    # your code goes here
    words = text_string.split()
    for i in range(len(words) - 1):
        ngram = tuple(words[i: i + n])
        if i >= len(words) - n:
            chains[ngram] = None
        else:
            nth_word = words[i + n]
            if ngram not in chains:
                chains[ngram] = [nth_word]
            else:
                chains[ngram].append(nth_word)
    return (chains, n)

def make_text(chains, n):
    """Return text from chains."""

    words = []

    capital_keys = [key for key in chains.keys() if key[0][0].isupper() and chains[key] != None]
    first_key = choice(capital_keys)

    words.extend(list(first_key))
    rand_value = choice(chains[first_key])
    words.append(rand_value)

    i = 1
    while len(words) < 50:
        new_key = tuple(words[i: i + n])
        if not chains[new_key]:
            break
        else:
            rand_value = choice(chains[new_key])
            words.append(rand_value)
            i += 1

    # words.append(rand_value)
    # link = (first_key[1], rand_value)
    # rand_value_2 = choice(chains[link])

    return " ".join(words)


input_path1 = sys.argv[1]
input_path2 = sys.argv[2]

# Open the file and turn it into one long string
combined_text = open_and_read_file(input_path1) + open_and_read_file(input_path2)

# Get a Markov chain
chains, number_ngram = make_chains(combined_text)

# Produce random text
random_text = make_text(chains, number_ngram)

print "\n", random_text
