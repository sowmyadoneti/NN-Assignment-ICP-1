import random
string = input("Enter a input string: ")
char_list = list(string)
if len(char_list) > 2:
    random_no_indexes=random.randrange(2, len(char_list))

    for i in range(random_no_indexes):
        random_index= random.randrange(len(char_list))
        del char_list[random_index]
    print(''.join(char_list[::-1]))
else: print("input string should have atleast 2 characters in the string")