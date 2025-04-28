a, b, c = map(int, input().split())
i=0
if 0==c and a==b:
    print("YES")
elif 0==c and a!=b:
    print("NO")
elif 0!=c:
    
    while i!=c:
        i+=1
        x=a-i
        z=b+i
        # print(x,z)
    if x==z:
        print("YES   ",i)
    else:
        print("NO")

# else:
#     i=0
#     while i!=c:
#         i+=1
#         x=a-i
#         z=b+i
#         # print(x,z)
#     if x==z:
#         print("YES")
#     else:
#         print("NO")