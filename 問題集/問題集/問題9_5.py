def plus(x,y):
   return x + y
def minus(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x // y
def remainder(x,y):
    return x % y
num1 = int(input("整数を入力してください："))
num2 = int(input("整数を入力してください："))
print(str(num1) + "+" + str(num2) + "=" + str(plus(num1,num2)))
print(str(num1) + "-" + str(num2) + "=" + str(minus(num1,num2)))
print(str(num1) + "*" + str(num2) + "=" + str(multiply(num1,num2)))
print(str(num1) + "/" + str(num2) + "=" + str(divide(num1,num2)))
print(str(num1) + "%" + str(num2) + "=" + str(remainder(num1,num2)))