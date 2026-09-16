a=int(input("Enter number a: "))
b=int(input("Enter number b: "))

print("Select Operation \n1.Addition \n2.Subtraction \n3.Multiplication \n4.Division \n5.Factorial")
choice=int(input("Enter your choice: "))

match choice:
    case 1:
        sum=a+b
        print(sum)
    case 2:
        diff=b-a
        print(diff)
    case 3:
        prod=a*b
        print(prod)
    case 4:
        div=b/a
        print(div)
    case 5:
        a=5
        fact=1
        i=1
        while i<=a:
            fact*=i
        print(fact)
    case _:
        pass