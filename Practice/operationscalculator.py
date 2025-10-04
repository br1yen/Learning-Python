operator = input('Enter a mode of operation (+ - * /):')
num1 = float(input("Enter 1st Number: "))
num2 = float(input("Enter a 2nd Number: "))

if operator == '+':
	result = num1 + num2
elif operator == '-':
	result = num1 - num2
elif operator == '*':
	result = num1*num2
elif operator == '/':
	result = num1/num2
else:
	print('Invalid input')

print(result)