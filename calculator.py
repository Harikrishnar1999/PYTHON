a=int(input("enter a value"))
b=int(input("enter second value"))
while True:
    print("\n main menu")
    print("1,addition")
    print("2,subtract")
    print("3,multiply")
    print("4,divide")
    print("5,exit")
    choose=int(input("enter your choice"))
    if choose==1:
        sum=a+b
        print("sum =",sum)
    elif choose==2:
        sub=a-b
        print("sub =",sub)
    elif choose==3:
        mult=a*b
        print("mult =",mult)
    elif choose==4:
        div=a%b
        print("div =",div)

    elif choose==5:
        break
    else:
        print("invalid choice")
