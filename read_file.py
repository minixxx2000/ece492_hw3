filename = 'sample_text.txt'

f = open(filename)

total = 0
times = 0
for line in f:
	if "X-DSPAM-Confidence: " in line:
		num = line.strip("X-DSPAM-Confidence: ")
		total = total + float(num)
		times = times + 1
f.close()
avg = str(total/times)
print "Average spam confidence: " , avg
