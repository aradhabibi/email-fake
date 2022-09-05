import random
import string
x = 0

def random_char(char_num):
       return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))
while x < 10:
       print (random_char(10)+"@gmail.com")
       x += 1
