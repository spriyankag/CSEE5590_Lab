#list of students in python class
python_students = ['priyanka', 'hema', 'sravya', 'amulya', 'pratyusha', 'bhargavi']

#list of students in web class
web_students = ['priyanka', 'hema', 'vineeth', 'sandeep', 'vinay']

#converting list to sets and printing the common students
print("Common students in both the class are:", set(python_students) & set(web_students))

#converting list to sets and printing the not in common students
print("Students that are not in common in both the classes are:",set(python_students) ^ set(web_students) )


