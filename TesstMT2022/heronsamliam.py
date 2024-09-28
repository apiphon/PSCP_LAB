'''samliam'''
def main(a,b,c):
    '''C:   2, 0: Missing function or method docstring'''
    s = (a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))**0.5
x=float(input())
y=float(input())
z=float(input())
cf=main(x,y,z)
print(f"{cf:.03f}")
