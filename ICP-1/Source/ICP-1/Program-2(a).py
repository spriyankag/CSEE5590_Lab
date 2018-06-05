#Initializing varibles and assigning them to user input
first_name = input("enter your first name:")
last_name = input("enter your last name:")

#list variable initialization
name = [ ]

#concatenating two variables
full_name = first_name + ' ' + last_name

#using split function
name = full_name.split(' ')

#using reverse function
reverse_order = name[::-1]

#using join function
full_name = ' '.join(reverse_order)

print(full_name)
