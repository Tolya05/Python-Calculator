def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def fourop():
	#Tells the user what the program is
	print("Hello and welcome to Anatoliy's CMD Calculator\n")
	#vars defined NOTE:check user inputs
  num1str = input("Number 1: ")
  if isfloat(num1str) == False:
    print("That's not a number")
    exit()
	num2str = input("Number 2: ")
  if isfloat(num2str) == False:
    print("That's not a number")
    exit()
  op = input("add, sub, mul, or div: ")

  num1 = float(num1str)
  num2 = float(num2str)

	#operations defined
	add = num1 + num2
	sub = num1 - num2
	mul = num1 * num2
	div = num1 / num2
  
  
	#does the operation
	if op == "add":
		print("You answwer is " + str(add))
	elif op == "sub":
		print("Your answer is " + str(sub))
	elif op == "mul":
		print("Your answer is " + str(mul))
	elif op == "div":
		print("Your answer is " + str(div))
	#if the user enters an incorrect operation
	else:
		print("Sorry the operation you entered was not correct, please try again")
