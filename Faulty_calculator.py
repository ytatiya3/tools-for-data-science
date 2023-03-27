#Exersise 2
#Design a calculator wich will correctly solve the problem except the following ones
#45*3 = 555, 56+9 = 77,56/6=4
# programme should take operator and the two numbers as the input from the user and then return the result

num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))

#opt = int(input("enter the operator you want to use \n 1 for + \n 2 for - \n 3 for * \n 4 for / \n 5 for ** \n"))
opt = input("select the operator\n + \n - \n * \n / \n ** \n % \n")

if num1 == 43 and num2 == 3 and opt == '*':
    result = 555
elif num1 == 56 and num2 == 9 and opt == '+':
    result = 77
elif num1 == 56 and num2 == 6 and opt == '/':
    result = 74
elif opt == '+':
    result = num1 + num2
elif opt == '-':
    result = num1 - num2
elif opt == '*':
    result = num1 * num2
elif opt == '/':
    result = num1 * num2
elif opt == '**':
    result = num1 ** num2
elif opt == '%':
    result = num1 % num2
else:
    print("enter the valid number")


print(result)

