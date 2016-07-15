def matrixmul():
    print("enter values")
    a=int(input("enter first elementin 1st row of m1"))
    b=int(input("enter second element in 1st row of m1"))
    c=int(input("enter first element in 2nd row of m1"))
    d=int(input("enter second element in 2nd row of m1"))
    e=int(input("enter first elementin 1st row of m2"))
    f=int(input("enter second element in 1st rowof m2"))
    g=int(input("enter first element in 2nd row of m2"))
    h=int(input("enter second element in 2nd row of m2"))
    firstelementR=(a*e) + (b*g)
    print(firstelementR),
    print ("\t"),
    secondelementR=(a*f) + (b*h)
    print(secondelementR),
    print ("\n"),
    thirdelementR=(c*e) + (d *g)
    print(thirdelementR),
    print ("\t"),
    fourthelementR=(c*f) + (d*h)
    print(fourthelementR)
    list1=[firstelementR,secondelementR]
    list2=[thirdelementR,fourthelementR]
    print("the matrix is as follows")
    print(list1)
    print(list2)
    
matrixmul()    
    
    
    
    
    
    