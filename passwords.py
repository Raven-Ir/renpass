import random
import string

def generated_password():
    string_pass = []

    character_len = random.randrange(7,10 )

    for i in range(0,character_len):
        string_pass.append(random.choice(string.ascii_letters))

    character_len = random.randrange(0,15-len(string_pass))

    for i in range(0,character_len):
        string_pass.append(random.randrange(0,9))
        
    
    character_len = 15 - len(string_pass)
    
    for i in range(0,character_len):
        string_pass.append(random.choice(string.punctuation))
    
    random.shuffle(string_pass)
    password = ''.join(map(str, string_pass))

    return password


def save_password(password):

    with open("pswrd.txt", "+a") as file:
        file.write(format(password))
        file.write("\n")
        print(file)
    

def show_password(key):
    file = open("pswrd.txt", "r")
    lines = file.read()
    print(lines)