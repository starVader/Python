# Enter your code here. Read input from STDIN. Print output to STDOUT
word = str(raw_input())
if (0 < len(word) < 1000):
    print word.isalnum()
    for i in word:
        if str(i).isaplha():
            print "True"
            break
    for i in word:
        if i.isdigit():
            print "True"
            break
    for i in word:
        if i.islower():
            print "True"
            break
    
    for i in word:
        if i.isupper():
            print "True"
            break
   
