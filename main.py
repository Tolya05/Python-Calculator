def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


#Tells the user what the program is
print("Hello and welcome to Anatoliy's CMD Calculator\n")
print("1 - add\n2 - subtract\n3 - multiply\n4 - divide\n")
op = input("Enter the number of the operation you want to do: ")
if isfloat(op) == False:
  print("That is not a valid operation :(")
  exit()
#vars defined NOTE:check user inputs
num1str = input("Number 1: ")
if isfloat(num1str) == False:
    print("That's not a number")
    exit()
num2str = input("Number 2: ")
if isfloat(num2str) == False:
    print("That's not a number")
    exit()


num1 = float(num1str)
num2 = float(num2str)
ops = float(op)

if ops == 4:
    if num2 == 0:
      print("%s / %s = undefined"%(num1, num2))
      exit()

#operations defined
add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

#does the operation
if ops == 1:
    print("%s + %s = %s"%(num1, num2, add))
elif ops == 2:
    print("%s - %s = %s"%(num1, num2, sub))
elif ops == 3:
    print("%s * %s = %s"%(num1, num2, mul))
elif ops == 4:
    print("%s / %s = %s"%(num1, num2, div))
#if the user enters an incorrect operation
else:
    print("Sorry the operation you entered was not correct, please try again")