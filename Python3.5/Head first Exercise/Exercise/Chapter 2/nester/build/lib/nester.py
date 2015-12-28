

def printmov(movie):
    for each in movie:
        if isinstance(each, list):
            printmov(each)
        else:
            print each


