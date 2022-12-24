import random
char_list = ['a', 'e', 'i', 'o', 'u']

for x in range(25):
    random.shuffle(char_list)
    print(''.join(char_list))