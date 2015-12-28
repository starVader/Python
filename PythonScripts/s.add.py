N = int(raw_input())
s = set()
if (0 < N < 1000):
    for i in range(N):
        inp = str(raw_input())
        s.add(inp)
    print len(s)
