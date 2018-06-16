import copy
user_input = input("type here!!!")
middle_word= []
reverse_words = []
words = user_input.split(" ")

#function to find middle one in the sentence
def find_middle_word(words):
    array_length = len(words)
    reminder = array_length % 2
    if (reminder == 0):
        quotient = int(array_length / 2)
        middle_word.append(words[quotient - 1])
        middle_word.append(words[quotient])
        print("middle words are:",middle_word)
    else:
        quotient = int(array_length // 2)
        middle_word.append(words[quotient])
        print("middle word", middle_word)


#function to find longest of all words
def find_longest_word(words):
    words_1 = copy.copy(words)
    words_1.sort(key=len)
    print("longest word in the sentence is:" , words_1[len(words_1)-1])

#function to get words in reverse order
def reverse_order(words):
    for i in words:
        rev = i[::-1]
        reverse_words.append(rev)
    sentence_reverse = " ".join(reverse_words)
    print("reverse order:",sentence_reverse)


#calling function from outside
find_middle_word(words)
find_longest_word(words)
reverse_order(words)

