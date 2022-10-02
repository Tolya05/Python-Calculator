def perr():
	expv = float(input("Enter your experimental value: "))
	extv = float(input("Enter the exact value: "))
	pe = ((expv - extv) / extv) * 100

	print("Your percent error is " + str(round(pe, 4)) + "%.")
