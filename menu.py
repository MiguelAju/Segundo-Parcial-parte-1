from random import* 

def opcionJugador():
    print("\t\t\tEscoje una opción\n")
    print("\t\t1). Piedra. 2). Papel. 3). Tijera.", end=' ')
    opcion = int(input("---> "))
    if opcion == 1:
        return "PIEDRA"
    elif opcion == 2:
        return "PAPEL"
    else :
        return "TIJERA"

def opcionMaquina():

    opcion = randint(1, 3)
    if opcion == 1:
        return "PIEDRA"
    elif opcion == 2:
        return "PAPEL"
    else :
        return "TIJERA"
# Se define el ganador
def ganador(player, pc):
    if player == pc:
        return "EMPATE"
        #jugar=input("Desea volver a jugar: s/n ")
 # -----------------------------
    if player == "PIEDRA" and pc == "PAPEL":
        return "La maquina GANA!"
    if player == "PIEDRA" and pc == "TIJERA":
        return "!GANASTE"
       # jugar=input("Desea volver a jugar: s/n ")
 # -----------------------------
    if player == "PAPEL" and pc == "PIEDRA":
        return "GANASTE!"
    if player == "PAPEL" and pc == "TIJERA":
        return "La maquina gana!"
       # jugar=input("Desea volver a jugar: s/n ")
 # -----------------------------
    if player == "TIJERA" and pc == "PIEDRA":
        return "La maquina gana!"
    if player == "TIJERA" and pc == "PAPEL":
        return "GANASTE!"
        #jugar=input("Desea volver a jugar: s/n ")
# Muestra el resultado
def resultado():
    j = opcionJugador()
    m = opcionMaquina()
    g = ganador(j, m)
    print("--------------------------------------")
    print("            |JUGADOR| VS |MAQUINA|")
    print("--------------------------------------")
    print("\t  ", j, "\t   ", m)
    print("\n\t\t   ", g)
    print("--------------------------------------")
    

resultado()
jugar='s'
while jugar=='s' or jugar=="S":
    jugar=input("Desea volver a jugar" "\t"'s/n:')
    if jugar=='s':
        resultado()
    #if jugar=='n':
     #   print("='(")
    #if jugar=='n':
     #   print("Feliz dia")
      #  break
else:
    print("!!Feliz día!!")
        