# Starting the calculator
k="Yes"
while k=="Yes":

    # Showing all available shapes
    print("Area Calculator")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Sqare")
    print("4. Parallelogram")
    print("5. Triangle")
    print("6. Rhombus")
    print("7. Trapezium")
    print("8. Ellipse")

     # Selecting a shape
    choice=int(input("Enter your Choice:"))

    #Circle Calculation
    if choice ==1:
        j=float(input("Enter Radius"))
        area=3.14*j*j
        print("Area of Circle=",area)

     #Rectangle Calculation
    elif choice==2:
        l=float(input("Enter length:"))
        b=float(input("Enter breadth:"))
        area=l*b
        print("Area of Rectangle =",area)

     #Square Calculation
    elif choice ==3:
        s=float(input("Enter side:"))
        area=s*s
        print("Area of Square=",area)

    #Parallelogram Calculation
    elif choice==4:
        b=float(input("Enter base:"))
        h=float(input("Enter height:"))
        area=b*h
        print("Area of Parallelogram=",area)

    #Triangle Calculation
    elif choice ==5:
        b=float(input("Enter base:"))
        h=float(input("Enter height:"))
        area= 0.5*b*h
        print("Area of triangle=",area)

     #Rhombus Calculation
    elif choice==6:
        a=float(input("Enter first diagnol:"))
        b=float(input("Enter second Diagnol:"))
        area=0.5*a*b
        print("Area of Rhombus=",area)
   
     #Trapezium Calculation
    elif choice==7:
        a=float(input("Enter first parallel side:"))
        b=float(input("Enter second parallel side:"))
        h=float(input("Enter height:"))
        area= 0.5*(a+b)*h
        print("Area of Trapezium =",area)

     #Ellipse Calculation
    elif choice==8:
        a=float(input("Enter semi-major axis:"))
        b=float(input("Enter semi-minor axis:"))
        area=3.14*a*b
        print("Area of Ellipse")

     # If the entered option is not available
    else:
        print("Invalid Choice")

    # Asking if the user wants to continue
    k=input("Do you want know the area of more shapes(Type Yes/No)")

    # Closing the program
    if k=="No" or "no":
        print("Thank you!!!")
        










    