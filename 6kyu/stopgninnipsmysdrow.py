"""
Write a function that takes in a string of one or more words, and returns the same string,
but with all five or more letter words reversed (Just like the name of this Kata).
Strings passed in will consist of only letters and spaces. Spaces will be included only 
when more than one word is present.
"""

# This is my solution:

def spin_words(sentence):
    """
    This function solve the problem above.

    Parameters:
    ----------

    sentence str: Sentence to spin


    Return:
    ----------

    str: Sentence spined
    """

    words = sentence.split()
    words = [word if len(word) < 5 else word[::-1] for word in words]
    return " ".join(words)



