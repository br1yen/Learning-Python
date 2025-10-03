def clean(s):
    sclean=s.translate(str.maketrans('\'\"!-?.,:;',9*' '))
    return sclean

string = input('Enter a strin:\n')
clean(string)
