import math

while True:
    print("Scegli la figura di cui calcolare il perimetro:\n A. Quadrato\n B. Cerchio\n C. Rettangolo\n")
    x = input ("Digita la tua selezione: ")
 
    if x == "A" or x == "a" :
        while True:
            try:
                l = int (input ("Inserisci il lato: "))
                if l<=0:
                    print("Il valore deve essere maggiore di zero, riprova.")
                else:    
                    perimetro1 = int (l*4)
                    print ("Il perimetro del quadrato è: " )
                    print (perimetro1)
                    break
            except ValueError:
                print("Input non valido, per favore inserisci un numero intero.")
        break    
 
    elif x == "B" or x == "b":
        while True:
            try:
                r = int (input ("Inserisci il raggio: "))
                if r<=0:
                    print("Il valore deve essere maggiore di zero, riprova.")
                else:
                    circonferenza = r * 2 * math.pi
                    print ("La circonferenza del cerchio è: ")
                    print (circonferenza)
                    break
            except ValueError:
                print("Input non valido, per favore inserisci un numero intero.")
        break    
 
    elif x == "C" or x == "c":
        while True:
            try:
                b = int (input ("Inserisci la base: "))
                h = int (input("Inserisci l'altezza: "))
                if b <= 0 or h<=0:
                    print("Il valore deve essere maggiore di zero, riprova.")
                else:
                    perimetro2 = b * 2 + h * 2
                    print ("Il perimetro del rettangolo è: " )
                    print (perimetro2)
                    break
            except ValueError:
                print("Input non valido, per favore inserisci un numero intero.")
        break        
    
    
 
    else:
        print ("Scelta non valida, per favore riprova")
        
    