a,b =map(int, input().split())
if b % 2 ==0:
    s=0
    for i in range(a,b+1,1):
        if i % 2 == 0:
            s+=1
            if s!=0:
                print(i)
            elif s == 0:
                print("   ")
elif b % 2 != 0:
    if a == b:
        print("   ")
    else:
        print(a+b)