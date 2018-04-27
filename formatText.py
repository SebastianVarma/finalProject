f = open("articleText.txt", "r")
lines = f.readlines()
f.close()

f = open("articleDatabase.txt", "r")
lines2 = f.readlines()
f.close()

f = open("articleText.txt", "w")
for line, line2 in zip(lines, lines2):
	if line2.split(" ")[0] == "http://cnn.com/" or line2.split(" ")[0] == "http://www.nytimes.com/":
		f.write("Reliable: " + "\n" + line)
		f.write("\n")
	else:
		f.write("Unreliable: " + "\n" + line)
		f.write("\n")
f.close()
