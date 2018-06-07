fh = open(r"C:\Users\mural\OneDrive\Desktop\s.txt", "r")

count = 0
data = fh.read()
each_line = data.split("\n")
#print(each_line)

for i in each_line:
    word = i.split(" ")
    print( " ".join(word), len(word))


