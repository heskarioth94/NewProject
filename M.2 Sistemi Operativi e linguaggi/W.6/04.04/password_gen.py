import string
import random


def password_gen():

    scelta = int(input("Questo programma serve per generare password!\n>>> 1 per una password di 8 caratteri\n>>> 2 per una password di 20 caratteri\nEffettua una scelta:\n>>>"))

    if scelta == 1:
        number_of_strings = 1
        length_of_string = 8
        for x in range(number_of_strings):
            print(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))

    elif scelta == 2:
        number_of_strings = 1
        length_of_string = 20
        for x in range(number_of_strings):
            print(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))

    else:
        print("Scelta non valida")

password_gen()
