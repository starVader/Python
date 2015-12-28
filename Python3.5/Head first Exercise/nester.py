
def printmov(movielist, indent = False ,level = 0):
    for each in movielist:
        if isinstance(each, list):
            printmov(each,indent ,level + 1)
        else:
            if indent== True:
                for i in range(level):
                    print ("\t",end ='')
            print (each)

movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
           ["Graham Chapman",
            ["Michael Palin", "John Cleese",    "Terry Gilliam", "Eric Idle", "Terry Jones"]]] 

printmov(movies, True, 1)
