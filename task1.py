# ------RANGE FUNCTION----------------#

for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        print(i, end=',')


# ---------------------FACTORIAL---------------------------------------#
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


a = input("Enter a number: ")
test_number = int(a)
result = factorial(test_number)
print("Factorial is:", result)


# -------------------DICTIONARY--------------------------------------#
numb=input("Enter the integral number:")
newDict = {}
for i in range(1, int(numb)+1):
    newDict[i] = i*i
print(newDict)


# ------------------------LIST & TUPLES----------------------------#
csvNumbers = input("Enter the sequence of numbers")
list1 = csvNumbers.split(',')
tuple1 = tuple(list1)
print(list1)
print(tuple1)
