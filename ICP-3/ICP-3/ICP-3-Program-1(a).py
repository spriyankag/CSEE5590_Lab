
user_input = input("entire the sentence:-")
#created a list and assigned the sentence to list
list_1 = user_input.split(" ")

#sorted list in ascending order
list_1.sort()

print(list_1)

#created a dictionary
frequency = dict()
count = 0

for i in list_1:
    frequency[i] = list_1.count(i)

print(frequency)








