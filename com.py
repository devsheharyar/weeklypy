x= int(input("Please enter the x number "))
y= int (input("Please enter the y number "))
def comparison (x,y):
    if x>y:
        print("x is bigger")
    elif y>x:
        print("y is bigger")
    elif x==y:
        print("both numbers are equal")

comparison(x,y)
