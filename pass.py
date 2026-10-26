import random
chars="abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
length=int(input("Enter Length :"))
password=""

for a in range(length):
    password+=random.choice(chars)
print(password)