#James Dutton
#ECE492 DISCUSSION14
total = 0
iterations = 0
with open("sample_text.txt","r") as f:
    for line in f:
        if "X-DSPAM-Confidence: " in line:
            line = line.strip("X-DSPAM-Confidence: ")
            total += float(line)
            iterations += 1

print("Average spam confidence is: " + str(total / iterations))
