print ("input lenghts of the triangle sides:")
x=int(input("x:"))
y=int(input("y:"))
z=int(input("y:"))
if x+y>z and y+z>x and x+z>y:
    if x==y and y==z and x==z:
        print("triangle is an equilateral triangle")
    elif x==y or y==z or x==z:
        print("triangle is an isocles triangle ")
    else:
        print("triangle is an scalene triangle")
else:

     print("please enter correct lenght of side")

