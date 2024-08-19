'''per8'''
def main():
    '''pepepe'''
    even_gift=0
    def loop(times,even_gift):
        if not times:
            return 1,even_gift
        x=int(input())
        if even_gift<x:
            even_gift=x
        return loop(times-1,even_gift)
    _, even_gift=loop(8,even_gift)
    print(even_gift)
main()
