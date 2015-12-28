N = int(raw_input())
result = []
pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
for i in range(N):
    email = str(raw_input())
    result.append(filter(map(lambda x: x , pattern) ,email))
print result    
