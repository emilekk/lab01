

num1=int(input("Первое число: "))
num2=int(input("Второе число: "))

while num1 != 0 and num2 != 0:
    if num1 >= num2:
        num1 %= num2
    else:
        num2 %= num1
if num1 !=0:
    print(num1)
else:
    print(num2)