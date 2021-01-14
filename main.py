from cryptography.fernet import Fernet

key = Fernet.generate_key()

crypter = Fernet(key)

pw = crypter.encrypt(b'MansiJain-MLSA')
decrypter = crypter.decrypt(pw)

print("This is your password: " + str(decrypter,'utf8'))
print("\n This is the encryption of that password: ")
print(str(pw,'utf8'))