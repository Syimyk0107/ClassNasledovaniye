def circle():
    x, y,z = map(int, input().split())
    r_circle = (x+y-z)/2    
    print(f"{r_circle:.6f}")
circle()
