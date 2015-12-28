# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
i = 0
percentage = 0
mydic = {}
for i in range(N):
    name,m1,m2,m3= map(str,raw_input().split())
    mydic[name] = {'sub1':m1,'sub2':m2,'sub3':m3}
find = raw_input()
for key in mydic:
        if (key == find):
            m1 = int(mydic[key].get('sub1'))
            m2 = int(mydic[key].get('sub2'))
            m3 = int(mydic[key].get('sub3'))
            percentage = (m1 + m2 +m3)*100
print "%.2f"% (percentage/300)

