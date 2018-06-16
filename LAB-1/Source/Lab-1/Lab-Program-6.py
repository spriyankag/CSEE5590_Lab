import numpy as np

#creating a random vector using random function
random_vector =np.random.randint(20,size=15)

#converting the vector into list
print(list(random_vector))

#counting the most frequenct number
count = np.bincount(random_vector).argmax()
print("Most frequent number:", count)


#
#







