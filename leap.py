'''9arm says pls use library calendar instead of write calendar with your self.'''
def maan():
    '''pep8naja'''
    yrs=float(input())
    if not yrs%400 and not yrs%100:
        print("Yes")
    elif not yrs%4 and yrs%100:
        print("Yes")
    else:
        print("No")
maan()
