def main():
    num = int(input("Enter a number: "))
    #escribe tu código abajo de esta línea
    if len(str(num))>6:
        print('Too long')
    else:
        if int(num)<0:
            num=str(num)[::-1]
            num=f"-{str(num)[:-1]}"
        else:
            num=str(num)[::-1]
        print(num)


if __name__=='__main__':
    main()
