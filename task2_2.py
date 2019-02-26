import math

c = 50
h = 30

d = input("enter the values: ")
list1 = d.split(',')
for i in list1:
    i = int(i)
    q = round(math.sqrt((2*c*i)/h))
    print(q, end=',')
