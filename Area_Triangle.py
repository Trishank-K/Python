x = float(input("Enter First Side : "))
y = float(input("Enter Second Side : "))
z = float(input("Enter Third Side : "))
s = (x+y+z)/2
temp = s*(s-x)*(s-y)*(s-z)
area = temp**0.5
print("Area : ", area)