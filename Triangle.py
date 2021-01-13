#To find area of triangle Given all three sides using Herons formula
x=int(input("Enter the First side of Triangle:"))
y=int(input("Enter the Second side of Triangle:"))
z=int(input("Enter the Third side of Triangle:"))
s=x+y+z/2
m=s*(s-x)*(s-y)*(s-z)**0.5
print("Area of Triangle is:",+m)
