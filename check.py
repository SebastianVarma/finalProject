f = open("articleDatabase.txt", "r")
lines2 = f.readlines()
f.close()

i = 0
for line2 in lines2:
	if line2.split(" ")[0] == "http://cnn.com/":
		i = i + 1
	
print(i)
