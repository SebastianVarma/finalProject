f = open("articleText.txt", "r")
lines = f.readlines()
f.close()

f = open("articleDatabase.txt", "r")
lines2 = f.readlines()
f.close()

i = 0
f = open("articleText.txt", "w")
for line, line2 in zip(lines, lines2):
	if i > 514:
		if line2.split(" ")[0] == "http://cnn.com/" or line2.split(" ")[0] == "http://www.nytimes.com/":
			f.write("(" + line.strip() + ") = 1")
			f.write("\n")
		else:
			f.write("(" + line.strip() + ") = 0")
			f.write("\n")
	i = i + 1
f.close()
