"""Traingle formation with *"""
         *
        * *
c = "*"
N = int(raw_input())
for i in range(N):
    print (c*i).rjust(N - 1)+c+(c*i).ljust(N - 1)
