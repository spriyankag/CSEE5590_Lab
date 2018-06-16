number_list = [1, 3, 6, 2, -1, 2, 8, -2, 9]

#empty tupple creation
triplets = ()
#empty list creation
triplet_list = []
for i in range(0,len(number_list)-2):
    for j in range(1,len(number_list)-1):
        for k in range(2,len(number_list)):
            addition = number_list[i] + number_list[j] + number_list[k]
            if(addition == 0):
                triplets = (number_list[i], number_list[j] , number_list[k])
                triplet_list.append(triplets)
                break
        break
print("Tripliets in the array list are:",triplet_list)

