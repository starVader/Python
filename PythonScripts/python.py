def startEndVowels(word):
        length = len(word)
        count = 0
        ch = word[0]
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        if ch in vowels:
                count = count +1
        ch = word[length - 1]
        if ch in vowels:
                count = count +1
        if count == 2:
                return "True"
        else:
                return "False"
