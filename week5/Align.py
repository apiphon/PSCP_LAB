'''gegrfdbverfd'''
def main():
    '''vefdjbvjwd'''
    size_text = int(input())
    location_text = str(input())
    mes_text = str(input())
    size_cen = (size_text - len(mes_text))//2
    if location_text == "left":
        print(f"{mes_text:<{size_text}}")
    elif location_text == "center":
        if not (size_text - len(mes_text))%2:
            print(" "*(size_cen),end="")
            print(mes_text,end="")
            print(" "*(size_cen),end="")
        else:
            print(" "*(size_cen),end=" ")
            print(mes_text,end="")
            print(" "*(size_cen),end="")
    elif location_text == "right":
        print(f"{mes_text:>{size_text}}")
main()
