fh = open(r"C:\Users\mural\OneDrive\Desktop\p.txt", "r")

data = fh.read()
words = data.split("\n")
new_file = open(r"C:\Users\mural\OneDrive\Desktop\m.txt", "w+")
for i in words:
    new_file.write(i + "-" + str(len(i)) )
    new_file.write('\n')



fh.close()

