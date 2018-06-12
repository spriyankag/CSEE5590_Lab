#enter user input
user_input = input("enter a sentence:-")

list_1 = list(user_input)

print(list_1)

#set creation and assignment
set_1 ={'a', 'e', 'i', 'o', 'u', 'A', 'e', 'i', 'o', 'u'}
vowel_count = 0

for alphabets  in list_1:
    if alphabets in set_1:
        vowel_count+=1

#print vowels count in sentence
print(vowel_count)




