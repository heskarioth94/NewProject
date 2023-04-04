import string
import random

def randomizer8():
    number_of_strings = 1
    length_of_string = 8
    for x in range(number_of_strings):
        print(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))
        
def randomizer20():
    number_of_strings = 1
    length_of_string = 20
    for x in range(number_of_strings):
        print(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))
        
        
def password_gen():
    
    scelta = input("Questo programma serve per generare password!\n>>> 1. per una password di 8 caratteri\n>>> 2. per una password di 20 caratteri\n>>> Q. Chiudi il programma\nEffettua una scelta:\n>>> ")

    if scelta == '1':
        length_of_string = 8
        print("La password generata è: ")
        randomizer8()

    elif scelta == '2':
        print("La password generata è: ")
        randomizer20()

    elif scelta == 'q' or scelta == 'Q':
        print("Hai terminato il programma")
        quit()

    else:
        print("Scelta non valida")

password_gen()
