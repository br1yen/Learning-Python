def clean(s):
    sclean=s.translate(str.maketrans('\'\"!-?.,:;',9*' '))
    return sclean

# the clean function makes use of the maketrans method
# maketrans a tabling method that takes two strings
# the first objects, and then the translation for them
# the translate method formally executes the cypher 