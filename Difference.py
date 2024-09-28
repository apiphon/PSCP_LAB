'''Difference'''
def main():
    ''''Difference'''
    n = int(input())
    m = int(input())
    a = set()
    b = set()
    for _ in range(n):
        ccc = int(input())
        a.add(ccc)
    for _ in range(m):
        ccd = int(input())
        b.add(ccd)
    e = a-b
    for i in sorted(e):
        print(i,end = " ")
main()
