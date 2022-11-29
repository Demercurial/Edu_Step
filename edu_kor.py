from math import *
def solve(a, b, c):
    d = b**2 - 4*a*c
    if d == 0:
        return -b/(2*a), -b/(2*a)
    elif d > 0:
        return min((-b-sqrt(d))/(2*a),(-b+sqrt(d))/(2*a)), max((-b-sqrt(d))/(2*a),(-b+sqrt(d))/(2*a))

a, b, c = int(input()), int(input()), int(input())
x1, x2 = solve(a, b, c)
print(x1, x2)