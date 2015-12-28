English = int(raw_input())
es = set(map(int,raw_input().split()))
French = int(raw_input())
fs = set(map(int,raw_input().split()))
print len(es.union(fs))

