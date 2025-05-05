while True:
        
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice=input("enter choices (1/2/3/4):")
    
    if choice not in["1","2","3","4"]:
        print("Invalid choice")
        break

    a=int(input("enter 1st integer:"))
    b=int(input("enter 2nd integer:"))

    match choice:
        case "1":
            print(a+b)
        case "2":
            print(a-b)
        case "3":
            print( a*b)
        case "4":
            if b==0:
                print("error! enter valid integer")
            else:
                print(a/b)
        case _:
            print("Invalid choice")
