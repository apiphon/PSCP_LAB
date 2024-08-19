'''Future Message'''


def main():
    '''isnumeric()'''
    x=str(input())
    if x.islower() is True:
        print("Lowercase")
    elif x.isupper() is True:
        print("Uppercase")
    elif x.istitle() is True:
        print("Title")
    elif x.isnumeric() is True:
        print("Number")
    elif x.isspace() is True:
        print("Space")
    else:
        print("Other")
main()
