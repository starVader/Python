#recursion reversal  strings

def revrec(st):
    if st == '':
        return ''
    else:
        first = st[0]
        return (revrec(st[1:])+first)
print (revrec('spam'))
