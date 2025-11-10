#types of triangles determinations
#determine by the three sides
#equivalent triangle = all sides are equal
#right angled triangle = a2 + b2 = c2
#isosceles triangle = two sides are equal
#scalene triangle = non equal triangle


def type_of_triangle():
    a = int(input("input the base of the triangle"))
    b = int(input("input the height/ one side of the triangle"))
    c = int(input("input the hypotenuse/ third side of the triangle"))
    
    #check for equivalent triangle
    if a==b==c:
        print("this triangle is a EQUIVALENT TRIANGLE and its area is")
    elif (a!=b and b!=c and a!=c) and not(a**2 + b**2 == c**2):
        print("this triangle is a SCALENE TRIANGLE and its area is")
    elif a==b or b==c or a==c:
        print("this triangle is an ISOSCELES TRIANGLE and its area is")
    elif a**2 + b**2 == c**2:
        print("this triangle is a RIGHT ANGLED TRIANGLE and its area is")
    else:
        print("not a triangle")
        
    def area_of_triangle():
        area = 0.5 * a * b
        print(area)
        
    area_of_triangle()
type_of_triangle()
        