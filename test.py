from cryptography.fernet import Fernet
from passwords import save_password, show_password, generated_password


password = generated_password()


key = Fernet.generate_key()
print(key)
fernet = Fernet(key)

encrypted_password = fernet.encrypt(password.encode())

decrypted = fernet.decrypt(encrypted_password).decode()

save_password(encrypted_password)
show_password(key)

#Links
#https://www.geeksforgeeks.org/how-to-encrypt-and-decrypt-strings-in-python/
#https://stackoverflow.com/questions/21916888/cant-concat-bytes-to-str

# TODO: Figure out the cryptography. The key could be stored in a hidden file. 