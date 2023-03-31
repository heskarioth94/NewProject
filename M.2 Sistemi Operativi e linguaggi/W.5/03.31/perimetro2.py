import math

gioco = True
while gioco:
    print("Scegli la figura di cui calcolare il perimetro:\n A. Quadrato\n B. Cerchio\n C. Rettangolo\n Q. Chiudi il programma")
    x = input ("Digita la tua selezione: ")
 
    if x == "A" or x == "a" :
        while gioco:
            try:
                l = int (input ("Inserisci il lato: "))
                if l<=0:
                    print("Il valore deve essere maggiore di zero, riprova.")
                else:    
                    perimetro1 = int (l*4)
                    print (f"Il perimetro del quadrato è:{perimetro1} " )
                    break
            except ValueError:
                print("Input non valido, per favore inserisci un numero intero.")
        break    
 
    elif x == "B" or x == "b":
        while gioco:
            try:
                r = int (input ("Inserisci il raggio: "))
                if r<=0:
                    print("Il valore deve essere maggiore di zero, riprova.")
                else:
                    circonferenza = r * 2 * math.pi
                    print (f"La circonferenza del cerchio è: {circonferenza} ")
                    break
            except ValueError:
                print("Input non valido, per favore inserisci un numero intero.")
        break    
 
    elif x == "C" or x == "c":
        while gioco:
            try:
                b = int (input ("Inserisci la base: "))
                h = int (input("Inserisci l'altezza: "))
                if b <= 0 or h<=0:
                    print("Il valore deve essere maggiore di zero, riprova.")
                else:
                    perimetro2 = b * 2 + h * 2
                    print (f"Il perimetro del rettangolo è: {perimetro2} " )

                    break
            except ValueError:
                print("Input non valido, per favore inserisci un numero intero.")
        break        

    elif x == "Q" or x == "q":
        gioco = False
        print ("Hai terminato il programma")
        break
 
    else:
        print ("Scelta non valida, per favore riprova")
       
    
