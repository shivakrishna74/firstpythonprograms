def caluculator():
    operator = ['+','-','/','%','*']
    print("choose operator")
    op = input("enter operator")
    num1=int(input("enter number"))
    num2=int(input("enter number"))
    if (op =='+'):
        num3 = num1 + num2
        print("%d + %d = %d" % (num1,num2,num3))
    elif(op =='-'):
        num3 = num1 - num2
        print("%d - %d = %d" % (num1,num2,num3))
    elif(op=='*'):
        num3 = num1 * num2
        print("%d * %d = %d" % (num1,num2,num3))
    
    
    else:
        print("operator does not exist")
        


caluculator()    