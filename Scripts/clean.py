def clean(s):
    sclean=s.translate(str.maketrans('\'\"!-?.,:;',9*' '))
    return sclean

string = input('Enter a string:\n')
clean(string)
