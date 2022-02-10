#!python3
#Thomas Cellitti 09/02/2022
#GitHub: thom0075
#Type of License: MIT
#This program must be executed using the terminal for efficiency and stability reasons

import math, turtle, random
from tqdm import tqdm
def quadrato(lato):
    for i in range(4):
        ninja.forward(lato)
        ninja.left(90)


def assi(maxx, maxy):
    ninja.penup()
    ninja.goto(0, maxy)
    ninja.pendown()
    ninja.goto(0, -1 * maxy)
    ninja.penup()
    ninja.goto(-1 * maxx, 0)
    ninja.pendown()
    ninja.goto(maxx, 0)


def cerchio(raggio, colore):
    ninja.pencolor(colore)
    ninja.begin_fill()
    ninja.circle(raggio)
    ninja.end_fill()

# Crea un oggetto Turtle chiamato "Ninja"
results = open("risultati.txt", "w")
ninja = turtle.Turtle()
#screen = turtle.Screen()
ninja.pensize(2)        #imposta la misura della penna
ninja.hideturtle()      #rende la tartaruga invisibil

ninja.pencolor("blue")  #imposta colore blu
assi(120, 120)          #chiama la funzione per disegnare gli assi
ninja.penup()           #solleva la penna
ninja.pencolor("red")   #cambia colore
ninja.goto(0, -100)     #va alle coordinate specficate
ninja.down()            #mette giu` la penna
ninja.circle(100)       #chiama la funzione circle per disegnare un cerchio
ninja.penup()           #solleva la penna
ninja.goto(0, 0)        #va alle coordinate specficate
ninja.down()
ninja.pencolor("black") 
quadrato(100)           #chiama la funzione quadrato per disegnare un quadrato
dentro = 0              #dichiara ed inizializza la variabile dentro
ninja.speed(0)          #imposta la velocita a 0 (piu` veloce)

n = int(input("Inserisci il numero di lanci da effettuare: "))  #dichiara ed inizializza la variabile n
#stato = 0
media = 0

for lanci in tqdm(range(n)):  #per ogni numero nel range 0-(n-1) rip
    x = random.randint(0, 100)  #genera delle coordinate random 
    y = random.randint(0, 100)
    ninja.penup()
    ninja.goto(x, y)
    ninja.pendown()
    #ninja.shape
    if 100**2 > x**2 + y**2:    #controlla se la somma di x^2 e y^2 e` minore di 100**2
        cerchio(0.5, "blue")    #disegna un cerchio di raggio 0.5 di colore blu
        dentro += 1             #incrementa di 1 la variabile dentro 
    else:                       #se la condizione dovesse risultare falsa disegna un cerchio verde
        cerchio(1, "green")
    pigreco = 4 * (dentro / (lanci + 1))    #calcola il valore di pi
    results.write(str(pigreco)+"\n")
    media+=pigreco
    #results.write(str(n)+"\n")
    #print("Pi Greco: %f"% (pigreco))        #stampa il valore calcolato
    #stato = math.round(((lanci/n)*100),2)
    #print(f"Stato: %f " %(round(((lanci/n)*100),3)), r"%")
    #print("n: %i" %(lanci))                     #stampa il valore di n (stringa di codice per debug)
media/=n
results.write("Media: %f" % (media))
print("Apri il file creato nella cartella di Python per visualizzare i risultati")
results.close()
