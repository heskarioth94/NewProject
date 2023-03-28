#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int scelta_menu;
    int punteggio = 0;
    char nome[50];

    printf("Benvenuto al nel quiz di cultura generale!\n");
    printf("Lo scopo del gioco e' di rispondere correttamente al maggior numero di domande possibile.\n");

    do {
        printf("\nMENU:\n");
        printf("1. Iniziare una nuova partita\n");
        printf("2. Uscire dal gioco\n");
        printf("Scegli: ");
        scanf("%d", &scelta_menu);

        if (scelta_menu == 1) {
            printf("\nInserisci il tuo nome: ");
            scanf("%s", nome);

            // Prima domanda
            printf("\nQunti giorni ci vogliono affinche' la terra graviti intorno al sole?\n");
            printf("A. 365\n");
            printf("B. 90\n");
            printf("C. 210\n");
            printf("D. 30\n");
            printf("Risposta: ");
            char risposta1;
            scanf(" %c", &risposta1);
            if (risposta1 == 'A' || risposta1 == 'a') {
                printf("Risposta corretta!\n");
                punteggio++;
            } else {
                printf("Risposta sbagliata!\n");
            }

            // Seconda domanda
            printf("\nQuale paese ha il maggior numero di isole al mondo?\n");
            printf("A. Italia\n");
            printf("B. Svezia\n");
            printf("C. Giappone\n");
            printf("D. Regno Unito\n");
            printf("Risposta: ");
            char risposta2;
            scanf(" %c", &risposta2);
            if (risposta2 == 'B' || risposta2 == 'b') {
                printf("Risposta corretta!\n");
                punteggio++;
            } else {
                printf("Risposta sbagliata!\n");
            }

            // Terza domanda
            printf("\nQual e' il continente piu' grande del mondo?\n");
            printf("A. Europa\n");
            printf("B. Africa\n");
            printf("C. Asia\n");
            printf("D. America\n");
            printf("Risposta: ");
            char risposta3;
            scanf(" %c", &risposta3);
            if (risposta3 == 'C' || risposta3 == 'c') {
                printf("Risposta corretta!\n");
                punteggio++;
            } else {
                printf("Risposta sbagliata!\n");
            }

            printf("\nHai totalizzato %d punti!\n", punteggio);

        } else if (scelta_menu == 2) {
            printf("\nGrazie per aver giocato! Arrivederci!\n");
            return 0;
        } else {
            printf("\nScelta non valida, riprova.\n");
        }

    } while (1);

    return 0;
}
