from tkinter import Y


x = input("Enter First Number : ") # 50
y = input ("Enter Second Number : ") # 60
print("x : ",x,"y : ",y)
x = int(x)+int(y) # 110
y = int(x)-int(y) # 110 - 60 = 50
x = int(x)-int(y)
print("x : ",x,"y : ",y)