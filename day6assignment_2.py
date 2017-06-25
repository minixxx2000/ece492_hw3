# Chia-Han Chen

hours = float(raw_input('Enter the number of hours:'))
rate = float(raw_input('Enter getting paid per hour:'))
total = hours*rate

if hours <= 40:
	print("Your total pay is: "+str(hours*rate))

else:
	overtime = hours - 40
	print("Your total pay is:"+str((hours-overtime)*rate+overtime*rate*1.5))
