t1,e1,f1 = map(int, input().split())
t2,e2,f2 = map(int, input().split())

s1 = t1*3+e1*20+f1*120
s2 = t2*3+e2*20+f2*120

if s1 > s2:
    print("Skimmer")
elif s1 < s2:
    print("Palka")
else:
    print("Draw")