"""
Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce
an output as shown below. Do not use the sum() function or a variable named sum in your solution.
"""
fname = input("Enter a filename: ")
fh = open(fname)
count = 0
s = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
	    continue
    m = line.rstrip()
    print("The Lines are: ", m)
    k = m.find("0")
    l = m[k:len(m)]
    j = float(l)
    s = s + j
    count = count + 1
print("Total sum of the number:", s)
print("Total number of lines:", count)
a = s/count
print("Average spam confidence:", round(a, 12))