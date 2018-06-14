import numpy as np

#random 2-dimensional matrix function
i=np.random.randint(100, size=(10,10))
p = np.array(i)
print(p)

list_1 = []


print("Minimum values in an array: ", i.min(axis = 1))
print("Maximum valuses in an array: ", i.max(axis = 1))
#conditional statements to retreive minimum value in each row
# for j in range(0,10):
#     for i in range(0,10):
#         #Aooendind each row into a list
#         list_1.append(p[j][i])
#     minimum = min(list_1)
#     maximum = max(list_1)
#     print("miminum value of row ", str(j) +   " is " + str(minimum))
#     print("maximum value of row ", str(j) +   " is " + str(maximum))
#     list_1 = []



