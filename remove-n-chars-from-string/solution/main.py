"""
Givet nedenstående tekststreng skal du lave en funktion, der tager en tekststreng og
et tal som argumenter, og som fjerner mængden af karakterer specificeret ved tallet.
"""

SENTENCE = "Hello Coding Pirates!"


def remove_chars(text, n):
    return text[n:]


text = remove_chars(SENTENCE, 6)

print(text)
