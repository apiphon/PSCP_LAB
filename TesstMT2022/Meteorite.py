'''Meteorite'''
def main():
    a = float(input())
    b = int(input())
    c = float(input())
    temp_a = a/b
    cxc = 0
    i = 1
    while temp_a > c:
        temp_a /= b
        cxc += 1*(i*b)
    print(cxc)
main()

