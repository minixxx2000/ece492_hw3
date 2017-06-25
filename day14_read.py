# Day 14 assignment
# Chia-Han, Chen
filename = 'sample_text.txt'

apple = open(filename)
total = 0
repeat = 0

for line in apple:
	if "X-DSPAM-Confidence: " in line:
		num = line.strip("X-DSPAM-Confidence: ")
		total = total + float(num)
		repeat = repeat + 1
		
apple.close()
print ("average spam confidence is: " + str(total/repeat))
