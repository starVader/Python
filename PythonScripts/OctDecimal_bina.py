N = int(raw_input())
length=len(bin(N))
width = length
if (1 <= N <= 99):
    for num in range(1,N+1):
        print('{0:{width}d} {0:{width}o} {0:{width}x} {0:{width}b}'.format(num,width=width))
     
