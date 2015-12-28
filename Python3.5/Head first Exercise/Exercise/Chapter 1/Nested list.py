

def printmov(movie):
    for each in movie:
        if isinstance(each, list):
            printmov(each)
        else:
            print each

movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
           ["Graham Chapman",
            ["Michael Palin", "John Cleese",    "Terry Gilliam", "Eric Idle", "Terry Jones"]]] 

printmov(movies)
