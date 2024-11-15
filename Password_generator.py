import random
import string

length = int(input("How many characters do you want? "))

characters = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits
password = ''.join(random.choice(characters) for _ in range(length))
password_list = list(password)
random.shuffle(password_list)
shuffled_password = ''.join(password_list)

print(shuffled_password)
