"""
Za otvaranje file-ova (koji imaju ime po sadržaju neke varijable):
(Za str samo makni ovo "f" i umjhesto {var1} napiši neki tekst)
var1 = "OVO JE TESTNA VARIJABLA"
with open(f"{var1}.txt", "w") as A:
    A.write("TEXT" + "\n")

Za ponovno otvaranje:
var1 = "OVO JE TESTNA VARIJABLA"
with open(f"{var1}.txt", "a") as A:
    A.write("TEKST1" + "\n")
"""

import os
import time
import tkinter as tk
from tkinter import messagebox


def skip(): #Za brisnaje printa
    for x in range(100):
        print(f"\n")

for filename in os.listdir(): #Za brisnje file-ova od prošle igre
    if filename.endswith(".txt"):
        os.remove(filename)


def unos_imena_igraca():
    I1 = input("Unesite ime 1. igrača: ")
    I2 = input("Unesite ime 2. igrača: ")
    I3 = input("Unesite ime 3. igrača: ")
    I4 = input("Unesite ime 4. igrača: ")
    I5 = input("Unesite ime 5. igrača: ")
    return I1, I2, I3, I4, I5

I1 = ""
I2 = ""
I3 = ""
I4 = ""
I5 = ""

"""
Z = Žito
K = Kamen
O = Ovca
C = Cigla
D = Drvo
B = bodovi
V = Broj viteških kartica iskorišteno
"""



# Igrač 1 (Drvo, cigla, kamen, ovca, žito i bodovi)
Z1 = 0
K1 = 0
O1 = 0
C1 = 0
D1 = 0
B1 = 0
V1 = 0
#Igrač 2 (Drvo, cigla, kamen, ovca, žito i bodovi)
Z2 = 0
K2 = 0
O2 = 0
C2 = 0
D2 = 0
B2 = 0
V1 = 0
# Igrač 3 (Drvo, cigla, kamen, ovca, žito i bodovi)
Z3= 0
K3 = 0
O3 = 0
C3 = 0
D3 = 0
B3 = 0
V1 = 0
# Igrač 4 (Drvo, cigla, kamen, ovca, žito i bodovi)
Z4 = 0
K4 = 0
O4 = 0
C4 = 0
D4 = 0
B4 = 0
V1 = 0
# Igrač 5 (Drvo, cigla, kamen, ovca, žito i bodovi)
Z5 = 0
K5 = 0
O5 = 0
C5 = 0
D5 = 0
B5 = 0
V1 = 0


def kreiranje_datoteka(I1, I2, I3, I4, I5):
    with open(f"{I1}.txt", "w"):
        pass

    with open(f"{I2}.txt", "w"):
        pass

    with open(f"{I3}.txt", "w"):
        pass

    with open(f"{I4}.txt", "w"):
        pass

    with open(f"{I5}.txt", "w"):
        pass

def gradnja():
    A1 = input("Unesite tip gradnje: ")

    if A1 == "Selo": #gradnja sela
        B = input("Unesite ime igrača:")
        if B == I1:
            if D1 >= 1 and C1 >= 1 and Z1 >= 1 and O1 >= 1:
                print(f"{I1} jr uspješno izgradio selo...")
                with open(f"{I1}.txt", "a") as A:
                    A.write("Gradnja sela " + "\n" + "+1 bod" + "\n")

                B1 = B1 + 1
                D1 = D1 - 1
                C1 = C1 - 1
                Z1 = Z1 - 1
                O1 = O1 - 1
        else:
            print("Pogreška u izgradnji! Nedovoljno materijala")

        if B == I2:
            if D2 >= 1 and C2 >= 1 and Z2 >= 1 and O2 >= 1:
                print(f"{I2} jr uspješno izgradio selo...")
                with open(f"{I2}.txt", "a") as B:
                    B.write("Gradnja sela " + "\n" + "+1 bod" + "\n")

                B2 = B2 + 1
                D2 = D2 - 1
                C2 = C2 - 1
                Z2 = Z2 - 1
                O2 = O2 - 1
        else:
            print("Pogreška u izgradnji! Nedovoljno materijala")

        if B == I3:
            if D3 >= 1 and C3 >= 1 and Z3 >= 1 and O3 >= 1:
                print(f"{I3} jr uspješno izgradio selo...")
                with open(f"{I3}.txt", "a") as A:
                    A.write("Gradnja sela " + "\n" + "+1 bod" + "\n")

                B3 = B3 + 1
                D3 = D3 - 1
                C3 = C3 - 1
                Z3 = Z3 - 1
                O3 = O3 - 1
        else:
            print("Pogreška u izgradnji! Nedovoljno materijala")

        if B == I4:
            if D4 >= 1 and C4 >= 1 and Z4 >= 1 and O4 >= 1:
                print(f"{I4} jr uspješno izgradio selo...")
                with open(f"{I4}.txt", "a") as A:
                    A.write("Gradnja sela " + "\n" + "+1 bod" + "\n")

                B4 = B4 + 1
                D4 = D4 - 1
                C4 = C4 - 1
                Z4 = Z4 - 1
                O4 = O4 - 1
        else:
            print("Pogreška u izgradnji! Nedovoljno materijala")

        """if B == I5:
            if D5 >= 1 and C5 >= 1 and Z5 >= 1 and O5 >= 1:
                print(f"{I5} jr uspješno izgradio selo...")
                with open(f"{I5}.txt", "a") as A:
                    A.write("Gradnja sela " + "\n" + "+1 bod" + "\n")

                B5 = B5 + 1
                D5 = D5 - 1
                C5 = C5 - 1
                Z5 = Z5- 1
                O5 = O5 - 1
        else:
            print("Pogreška u izgradnji! Nedovoljno materijala")"""



    if A1 == "Grad": #Gradnja grada
        B = input("Unesite ime igrača:")
        if B == I1:
            if K1 >= 3 and Z1 >= 2:
                print(f"{I1} jr uspješno izgradio grad...")
                with open(f"{I1}.txt", "a") as A:
                    A.write("Gradnja grada " + "\n" + "+2 boda" + "\n")

                B1 = B1 + 2
                K1 = K1 - 3
                Z1 = Z1 - 2

        else:
            print("Pogreška u izgradnji! Nedovoljno materijala")

        if B == I2:
            if K2 >= 3 and Z2 >= 2 :
                print(f"{I2} jr uspješno izgradio grad...")
                with open(f"{I2}.txt", "a") as A:
                    B.write("Gradnja grada " + "\n" + "+2 boda" + "\n")

                B2 = B2 + 2

                K2 = K2 - 3
                Z2 = Z2 - 2

        else:
            print("Pogreška u izgradnji! Nedovoljno materijala")

        if B == I3:
            if K3 >= 3  and Z3 >= 2:
                print(f"{I3} jr uspješno izgradio grad...")
                with open(f"{I3}.txt", "a") as A:
                    A.write("Gradnja grada " + "\n" + "+2 boda" + "\n")


                B3 = B3 + 2
                K3 = K3 - 3
                Z3 = Z3 - 2

        else:
            print("Pogreška u izgradnji! Nedovoljno materijala")

        if B == I4:
            if D4 >= 1 and C4 >= 1 and Z4 >= 1 and O4 >= 1:
                print(f"{I4} jr uspješno izgradio grad...")
                with open(f"{I4}.txt", "a") as A:
                    A.write("Gradnja grada " + "\n" + "+2 boda" + "\n")

                B4 = B4 + 2
                K4 = K4 - 3
                Z4 = Z4 - 2
        else:
            print("Pogreška u izgradnji! Nedovoljno materijala")

        """if B == I5:
            if D5 >= 1 and C5 >= 1 and Z5 >= 1 and O5 >= 1:
                print(f"{I5} jr uspješno izgradio grad...")
                with open(f"{I5}.txt", "a") as A:
                    A.write("Gradnja grada " + "\n" + "+2 boda" + "\n")

                B5 = B5 + 2
                K5 = K5 - 3
                Z5 = Z5 - 2
        else:
            print("Pogreška u izgradnji! Nedovoljno materijala")"""

    if A1 == "Cesta": #Gradnja ceste
        B = input("Unesite ime igrača: ")

        if B == I1:
            if C1 >= 1 and D1 >= 1:
                print(f"{I1} je uspješno izgradio cestu...")
                with open(f"{I1}.txt", "a") as A:
                    A.write("Gradnja ceste" + "\n")

                D1 = D1 - 1
                C1 = C1 - 1

            else:
                print("Pogreška u gradnji! Nedovoljno materijala")

        if B == I2:
            if C2 >= 1 and D2 >= 1:
                print(f"{I2} je uspješno izgradio cestu...")
                with open(f"{I2}.txt", "a") as A:
                    A.write("Gradnja ceste" + "\n")

                D2 = D2 - 1
                C2 = C2 - 1

            else:
                print("Pogreška u gradnji! Nedovoljno materijala")

        if B == I3:
            if C3 >= 1 and D3 >= 1:
                print(f"{I3} je uspješno izgradio cestu...")
                with open(f"{I3}.txt", "a") as A:
                    A.write("Gradnja ceste" + "\n")

                D3 = D3 - 1
                C3 = C3 - 1

            else:
                print("Pogreška u gradnji! Nedovoljno materijala")

        if B == I4:
            if C4 >= 1 and D4 >= 1:
                print(f"{I4} je uspješno izgradio cestu...")
                with open(f"{I4}.txt", "a") as A:
                    A.write("Gradnja ceste" + "\n")

                D4 = D4 - 1
                C4 = C4 - 1
            else:
                print("Pogreška u gradnji! Nedovoljno materijala")

       #
       # if B == I5:
       #      if C5 >= 1 and D5 >= 1:
       #          print(f"{I5} je uspješno izgradio cestu...")
       #          with open(f"{I5}.txt", "a") as A:
       #              A.write("Gradnja ceste" + "\n")
       #
       #          D5 = D5 - 1
       #          C5 = C5 - 1
       #
       #      else:
       #          print("Pogreška u gradnji! Nedovoljno materijala")
       #



    if A1 == "Brod": #Gradnja ceste
        B = input("Unesite ime igrača: ")

        if B == I1:
            if O1 >= 1 and D1 >= 1:
                print(f"{I1} je uspješno izgradio brod...")
                with open(f"{I1}.txt", "a") as A:
                    A.write("Gradnja broda" + "\n")

                D1 = D1 - 1
                O1 = O1 - 1

            else:
                print("Pogreška u gradnji! Nedovoljno materijala")

        if B == I2:
            if C2 >= 1 and D2 >= 1:
                print(f"{I2} je uspješno izgradio brod...")
                with open(f"{I2}.txt", "a") as A:
                    A.write("Gradnja broda" + "\n")

                D2 = D2 - 1
                O2 = O2 - 1

            else:
                print("Pogreška u gradnji! Nedovoljno materijala")

        if B == I3:
            if O3 >= 1 and D3 >= 1:
                print(f"{I3} je uspješno izgradio brod...")
                with open(f"{I3}.txt", "a") as A:
                    A.write("Gradnja broda" + "\n")

                D3 = D3 - 1
                O3 = O3 - 1

            else:
                print("Pogreška u gradnji! Nedovoljno materijala")

        if B == I4:
            if O4 >= 1 and D4 >= 1:
                print(f"{I4} je uspješno izgradio brod...")
                with open(f"{I4}.txt", "a") as A:
                    A.write("Gradnja broda" + "\n")

                D4 = D4 - 1
                O4 = O4 - 1

            else:
                print("Pogreška u gradnji! Nedovoljno materijala")

        """if B == I5:
            if O5 >= 1 and D5 >= 1:
                print(f"{I5} je uspješno izgradio brod...")
                with open(f"{I5}.txt", "a") as A:
                    A.write("Gradnja broda" + "\n")

                D5 = D5 - 1
                O5 = O5 - 1

            else:
                print("Pogreška u gradnji! Nedovoljno materijala")"""




def kartica_razvoja(): #kupnja kartice razvoja
    B = input("Unesite ime igrača: ")
    if B == I1:
        if Z1 >= 1 and O1 >= 1 and K1 >= 1:
            print(f"{I1} je uspješno kupio karticu razvoja...")
            with open(f"{I1}.txt", "a") as A:
                A.write("Kupljena kartica razvoja" + "\n")

            K1 = K1 - 1
            Z1 = Z1 - 1
            O1 = O1 - 1

        else:
            print("Kupnja nije uspjela! Nedovoljno materijala")

    if B == I2:
        if Z2 >= 1 and O2 >= 1 and K2 >= 1:
            print(f"{I1} je uspješno kupio karticu razvoja...")
            with open(f"{I2}.txt", "a") as A:
                A.write("Kupljena kartica razvoja" + "\n")

            K2 = K2 - 1
            Z2 = Z2 - 1
            O2 = O2 - 1

        else:
            print("Kupnja nije uspjela! Nedovoljno materijala")

    if B == I3:
        if Z3 >= 1 and O3 >= 1 and K3 >= 1:
            print(f"{I3} je uspješno kupio karticu razvoja...")
            with open(f"{I3}.txt", "a") as A:
                A.write("Kupljena kartica razvoja" + "\n")

            K3 = K3 - 1
            Z3 = Z3 - 1
            O3 = O3 - 1

        else:
            print("Kupnja nije uspjela! Nedovoljno materijala")

    if B == I4:
        if Z4 >= 1 and O4 >= 1 and K4 >= 1:
            print(f"{I4} je uspješno kupio karticu razvoja...")
            with open(f"{I4}.txt", "a") as A:
                A.write("Kupljena kartica razvoja" + "\n")

            K4 = K4 - 1
            Z4= Z4 - 1
            O4 = O4 - 1

        else:
            print("Kupnja nije uspjela! Nedovoljno materijala")

    """if B == I5:
        if Z5 >= 1 and O5 >= 1 and K5 >= 1:
            print(f"{I5} je uspješno kupio karticu razvoja...")
            with open(f"{I5}.txt", "a") as A:
                A.write("Kupljena kartica razvoja" + "\n")

            K5 = K5 - 1
            Z5 = Z5 - 1
            O5 = O5 - 1

        else:
            print("Kupnja nije uspjela! Nedovoljno materijala")"""


def aktivacija_kartice_razvoja(): #Kada netko iskoristi karticu razvoj ovo se pokreće
    B = input("Unesite ime igrača: ")

    if B == I1:
        C = input("Unesite tip kartice: ")

        if C == "Bodovi": #kartica na kojim piše bodovi

            D = int(input("Unesite broj bodova: "))
            with open(f"{I1}.txt", "a") as A:
                A.write("Iskorištena kartica razvoja: BODOVI:")
            print(f"{I1} je dobio {D} bodova...")
            with open(f"{I1}.txt", "a") as A:
                A.write(f"  +{D} bodova" + "\n")

            B1 = B1 + D


        if C == "Izum": #Kartica izum
            with open(f"{I1}.txt", "a") as A:
                A.write("Iskorištena kartica razvoja: IZUM:" + "\n")
            for Y in range(1, 2, 1):
                F = input(f"Unesite tip {Y}-te kartice:")


                if f == "Žito":
                    Z1 = Z1 + 1
                    with open(f"{I1}.txt", "a") as A:
                        A.write("   +1 Žito" + "\n")

                if f == "Kamen":
                    K1 = K1 + 1
                    with open(f"{I1}.txt", "a") as A:
                        A.write("   +1 Kamen" + "\n")

                if f == "Cigla":
                    C1 = C1 + 1
                    with open(f"{I1}.txt", "a") as A:
                        A.write("   +1 Cigla" + "\n")

                if f == "Drvo":
                    D1 = D1 + 1
                    with open(f"{I1}.txt", "a") as A:
                        A.write("   +1 Drvo" + "\n")

                if f == "Ovca":
                    O1 = O1 + 1
                    with open(f"{I1}.txt", "a") as A:
                        A.write("   +1 Ovca" + "\n")


        if C == "Vitez":
            with open(f"{I1}.txt", "a") as A:
                A.write("Iskorištena kartica razvoja: VITEZ" + "\n")


        if C == "Gradnja Cesta":
            with open(f"{I1}.txt", "a") as A:
                A.write("Kartica razvoja: GRADNJA CESTA" + "\n")
                A.write("Igrađene 2 ceste" + "\n")


    if B == I2:
        C = input("Unesite tip kartice: ")

        if C == "Bodovi": #kartica na kojim piše bodovi

            D = int(input("Unesite broj bodova: "))
            with open(f"{I2}.txt", "a") as A:
                A.write("Iskorištena kartica razvoja: BODOVI:")
            print(f"{I2} je dobio {D} bodova...")
            with open(f"{I2}.txt", "a") as A:
                A.write(f"  +{D} bodova" + "\n")

            B2 = B2 + D


        if C == "Izum": #Kartica izum
            with open(f"{I2}.txt", "a") as A:
                A.write("Iskorištena kartica razvoja: IZUM:" + "\n")
            for Y in range(1, 2, 1):
                F = input(f"Unesite tip {Y}-te kartice:")


                if f == "Žito":
                    Z1 = Z1 + 1
                    with open(f"{I2}.txt", "a") as A:
                        A.write("   +1 Žito" + "\n")

                if f == "Kamen":
                    K1 = K1 + 1
                    with open(f"{I2}.txt", "a") as A:
                        A.write("   +1 Kamen" + "\n")

                if f == "Cigla":
                    C1 = C1 + 1
                    with open(f"{I2}.txt", "a") as A:
                        A.write("   +1 Cigla" + "\n")

                if f == "Drvo":
                    D1 = D1 + 1
                    with open(f"{I2}.txt", "a") as A:
                        A.write("   +1 Drvo" + "\n")

                if f == "Ovca":
                    O1 = O1 + 1
                    with open(f"{I2}.txt", "a") as A:
                        A.write("   +1 Ovca" + "\n")


        if C == "Vitez":
            with open(f"{I2}.txt", "a") as A:
                A.write("Iskorištena kartica razvoja: VITEZ" + "\n")


        if C == "Gradnja Cesta":
            with open(f"{I2}.txt", "a") as A:
                A.write("Kartica razvoja: GRADNJA CESTA" + "\n")
                A.write("Igrađene 2 ceste" + "\n")



    if B == I3:
        C = input("Unesite tip kartice: ")

        if C == "Bodovi": #kartica na kojim piše bodovi

            D = int(input("Unesite broj bodova: "))
            with open(f"{I3}.txt", "a") as A:
                A.write("Iskorištena kartica razvoja: BODOVI:")
            print(f"{I3} je dobio {D} bodova...")
            with open(f"{I3}.txt", "a") as A:
                A.write(f"  +{D} bodova" + "\n")

            B3 = B3 + D


        if C == "Izum": #Kartica izum
            with open(f"{I3}.txt", "a") as A:
                A.write("Iskorištena kartica razvoja: IZUM:" + "\n")
            for Y in range(1, 2, 1):
                F = input(f"Unesite tip {Y}-te kartice:")


                if f == "Žito":
                    Z1 = Z1 + 1
                    with open(f"{I3}.txt", "a") as A:
                        A.write("   +1 Žito" + "\n")

                if f == "Kamen":
                    K1 = K1 + 1
                    with open(f"{I3}.txt", "a") as A:
                        A.write("   +1 Kamen" + "\n")

                if f == "Cigla":
                    C1 = C1 + 1
                    with open(f"{I3}.txt", "a") as A:
                        A.write("   +1 Cigla" + "\n")

                if f == "Drvo":
                    D1 = D1 + 1
                    with open(f"{I3}.txt", "a") as A:
                        A.write("   +1 Drvo" + "\n")

                if f == "Ovca":
                    O1 = O1 + 1
                    with open(f"{I3}.txt", "a") as A:
                        A.write("   +1 Ovca" + "\n")


        if C == "Vitez":
            with open(f"{I3}.txt", "a") as A:
                A.write("Iskorištena kartica razvoja: VITEZ" + "\n")


        if C == "Gradnja Cesta":
            with open(f"{I3}.txt", "a") as A:
                A.write("Kartica razvoja: GRADNJA CESTA" + "\n")
                A.write("Igrađene 2 ceste" + "\n")




    if B == I4:
        C = input("Unesite tip kartice: ")

        if C == "Bodovi": #kartica na kojim piše bodovi

            D = int(input("Unesite broj bodova: "))
            with open(f"{I4}.txt", "a") as A:
                A.write("Iskorištena kartica razvoja: BODOVI:")
            print(f"{I4} je dobio {D} bodova...")
            with open(f"{I4}.txt", "a") as A:
                A.write(f"  +{D} bodova" + "\n")

            B4 = B4 + D


        if C == "Izum": #Kartica izum
            with open(f"{I4}.txt", "a") as A:
                A.write("Iskorištena kartica razvoja: IZUM:" + "\n")
            for Y in range(1, 2, 1):
                F = input(f"Unesite tip {Y}-te kartice:")


                if f == "Žito":
                    Z1 = Z1 + 1
                    with open(f"{I4}.txt", "a") as A:
                        A.write("   +1 Žito" + "\n")

                if f == "Kamen":
                    K1 = K1 + 1
                    with open(f"{I4}.txt", "a") as A:
                        A.write("   +1 Kamen" + "\n")

                if f == "Cigla":
                    C1 = C1 + 1
                    with open(f"{I4}.txt", "a") as A:
                        A.write("   +1 Cigla" + "\n")

                if f == "Drvo":
                    D1 = D1 + 1
                    with open(f"{I4}.txt", "a") as A:
                        A.write("   +1 Drvo" + "\n")

                if f == "Ovca":
                    O1 = O1 + 1
                    with open(f"{I4}.txt", "a") as A:
                        A.write("   +1 Ovca" + "\n")


        if C == "Vitez":
            with open(f"{I4}.txt", "a") as A:
                A.write("Iskorištena kartica razvoja: VITEZ" + "\n")


        if C == "Gradnja Cesta":
            with open(f"{I4}.txt", "a") as A:
                A.write("Kartica razvoja: GRADNJA CESTA" + "\n")
                A.write("Igrađene 2 ceste" + "\n")



def Nagrade():
    B = input("Unesite tip nagrade: ")
    C = input("Unesite ime igrača:")

    if B == "Najduža Cesta":
        if C == I1:
            B1 = B1 + 2
            with open(f"{I1}.txt", "a") as A:
                A.write("Najduža cesta, +2 boda", "\n")

        if C == I2:
            B2 = B2 + 2
            with open(f"{I2}.txt", "a") as A:
                A.write("Najduža cesta, +2 boda" + "\n")

        if C == I3:
            B3 = B3 + 2
            with open(f"{I3}.txt", "a") as A:
                A.write("Najduža cesta, +2 boda", "\n")

        if C == I4:
            B4 = B4 + 2
            with open(f"{I4}.txt", "a") as A:
                A.write("Najduža cesta, +2 boda", "\n")

    if B == "Viteška moć":
        if C == I1:
            B1 = B1 + 2
            with open(f"{I1}.txt", "a") as A:
                A.write("Najveća viteška moć, +2 boda", "\n")

        if C == I2:
            B2 = B2 + 2
            with open(f"{I2}.txt", "a") as A:
                A.write("Najveća viteška moć, +2 boda" + "\n")

        if C == I3:
            B3 = B3 + 2
            with open(f"{I3}.txt", "a") as A:
                A.write("Najveća viteška moć, +2 boda", "\n")

        if C == I4:
            B4 = B4 + 2
            with open(f"{I4}.txt", "a") as A:
                A.write("Najveća viteška moć, +2 boda", "\n")

def oduzimanje_nagrada():
    B = input("Unesite tip nagrade koju želite oduzeti: ")
    C = input("Unesite time igrača: ")

    if B == "Najduža cesta":
        if C == I1:
            B1 = B1 - 2
            with open(f"{I1}.txt", "a") as A:
                A.write("Oduzimanje nagrade za najdužu cestu, -2 boda" + "\n")

        if C == I2:
            B2 = B2 - 2
            with open(f"{I2}.txt", "a") as A:
                A.write("Oduzimanje nagrade za najdužu cestu, -2 boda" + "\n")

        if C == I3:
            B3 = B3 - 2
            with open(f"{I3}.txt", "a") as A:
                A.write("Oduzimanje nagrade za najdužu cestu, -2 boda" + "\n")

        if C == I4:
            B4 = B4 - 2
            with open(f"{I4}.txt", "a") as A:
                A.write("Oduzimanje nagrade za najdužu cestu, -2 boda" + "\n")

    if B == "Viteška moč":
        if C == I1:
            B1 = B1 - 2
            with open(f"{I1}.txt", "a") as A:
                A.write("Oduzimanje nagrade za največu vitešku moć, -2 boda" + "\n")

        if C == I2:
            B2 = B2 - 2
            with open(f"{I2}.txt", "a") as A:
                A.write("Oduzimanje nagrade za največu vitešku moć, -2 boda" + "\n")

        if C == I3:
            B3 = B3 - 2
            with open(f"{I3}.txt", "a") as A:
                A.write("Oduzimanje nagrade za največu vitešku moć, -2 boda" + "\n")

        if C == I4:
            B4 = B4 - 2
            with open(f"{I4}.txt", "a") as A:
                A.write("Oduzimanje nagrade za največu vitešku moć, -2 boda" + "\n")





# import tkinter as tk
# from PIL import Image, ImageTk
# from tkinter import messagebox
# def quit_window():
#
#     response = messagebox.askquestion("Catan Management System", "Do you want to end the game?")
#     if response == 'yes':
#         root.quit()
#
#
#
#
# def display_image(image_path):
#     global image_label  # Declare image_label as a global variable
#     # Load the image
#     image = Image.open(image_path)
#     photo = ImageTk.PhotoImage(image)
#
#     # Update the label with the new image
#     image_label.config(image=photo)
#     image_label.image = photo  # This line is necessary to prevent garbage collection
#
# # Create a Tkinter window
# root = tk.Tk()
# root.title("Image Display Example")
#
# # Initial image path
# initial_image_path = "pomorci menu.jpg"
#
# # Create a label widget to display the image
# image_label = tk.Label(root)
# image_label.pack()
#
# # Load and display the initial image
# display_image(initial_image_path)
#
# # Quit button
# quit_button = tk.Button(root, text="Quit", command=quit_window)
# quit_button.pack(side=tk.LEFT, padx=10)
#
#
# # Run the Tkinter event loop
# root.mainloop()


# def player1():
#     II1 = 0
#     while II1 == 0:
#         KI1 = input("Unesite komandu: ")
#         if KI1 == "Aktivacija Kartice Razvoja":
#             aktivacija_kartice_razvoja()
#
#         if KI1 == "Sljedeći igrač":
#             II1 = 1
#
#         if KI1 == "Kupnja Kartice Razvoja":
#             kartica_razvoja()
#
#         if KI1 == "Gradnja":
#             gradnja()
#
#         if KI1 == "Nagrada":
#             Nagrade()
#
#         if KI1 == "Dobivanje":
#
#             H = input("Unesite tip kartice: ")
#             KD = int(input("Unesite količinu: "))
#             KDA = str(KD)
#             with open(f"{I1}.txt", "a") as A:
#                 A.write("dobivanje: " + H + "" + KDA + "\n")
#                 if H == "Žito":
#                     Z1 = Z1 + KD
#
#                 if H == "Kamen":
#                     K1 = K1 + KD
#
#                 if H == "Drvo":
#                     D1 = D1 + KD
#
#                 if H == "Cigla":
#                     C1 = C1 + KD
#
#                 if H == "Ovca":
#                     O1 = O1 + KD
#
#         if KI1 == "Gubljenje":
#             H = input("Unesite tip kartice: ")
#             KD = int(("Unesite količinu: "))
#             with open(f"{I1}.txt", "a") as A:
#                 A.write("dobivanje: " + H + "" + D + "\n")
#                 if H == "Žito":
#                     Z1 = Z1 - KD
#
#                 if H == "Kamen":
#                     K1 == K1 - KD
#
#                 if H == "Drvo":
#                     D1 == D1 - KD
#
#                 if H == "Cigla":
#                     C1 = C1 - KD
#
#                 if H == "Ovca":
#                     O1 = O1 - KD
#
#     if II1 == 1:
#         player2()
#
#     if B1 >= 12:
#         exit(f"{I1} je pobjedio")
#
#     def player2():
#         II1 = 0
#         while II1 == 0:
#             KI1 = input("Unesite komandu: ")
#             if KI1 == "Aktivacija Kartice Razvoja":
#                 aktivacija_kartice_razvoja()
#
#             if KI1 == "Sljedeći igrač":
#                 II1 = 1
#
#             if KI1 == "Kupnja Kartice Razvoja":
#                 kartica_razvoja()
#
#             if KI1 == "Gradnja":
#                 gradnja()
#
#             if KI1 == "Nagrada":
#                 Nagrade()
#
#             if KI1 == "Dobivanje":
#
#                 H = input("Unesite tip kartice: ")
#                 KD = int(("Unesite količinu: "))
#                 with open(f"{I2}.txt", "a") as A:
#                     A.write("dobivanje: " + H + "" + D + "\n")
#                     if H == "Žito":
#                         Z2 = Z2 + KD
#
#                     if H == "Kamen":
#                         K2 == K2 + KD
#
#                     if H == "Drvo":
#                         D2 == D2 + KD
#
#                     if H == "Cigla":
#                         C2 = C2 + KD
#
#                     if H == "Ovca":
#                         O2 = O2 + KD
#
#             if KI1 == "Gubljenje":
#                 H = input("Unesite tip kartice: ")
#                 KD = int(("Unesite količinu: "))
#                 with open(f"{I2}.txt", "a") as A:
#                     A.write("dobivanje: " + H + "" + D + "\n")
#                     if H == "Žito":
#                         Z2 = Z2 - KD
#
#                     if H == "Kamen":
#                         K2 == K2 - KD2
#                     if H == "Drvo":
#                         D2 == D2 - KD
#
#                     if H == "Cigla":
#                         C2 = C2 - KD
#
#                     if H == "Ovca":
#                         O2 = O2 - KD
#
#     if II1 == 1:
#         player3()
#
#     if B2 >= 12:
#         exit(f"{I2} je pobjedio")
#
#
#
#
#
# def player3():
#     II1 = 0
#     while II1 == 0:
#         KI1 = input("Unesite komandu: ")
#         if KI1 == "Aktivacija Kartice Razvoja":
#             aktivacija_kartice_razvoja()
#
#         if KI1 == "Sljedeći igrač":
#             II1 = 1
#
#         if KI1 == "Kupnja Kartice Razvoja":
#             kartica_razvoja()
#
#         if KI1 == "Gradnja":
#             gradnja()
#
#         if KI1 == "Nagrada":
#             Nagrade()
#
#         if KI1 == "Dobivanje":
#
#             H = input("Unesite tip kartice: ")
#             KD = int(("Unesite količinu: "))
#             with open(f"{I3}.txt", "a") as A:
#                 A.write("dobivanje: " + H + "" + D + "\n")
#                 if H == "Žito":
#                     Z3 = Z3 + KD
#
#                 if H == "Kamen":
#                     K3 == K3 + KD
#
#                 if H == "Drvo":
#                     D3 == D3 + KD
#
#                 if H == "Cigla":
#                     C3 = C3 + KD
#
#                 if H == "Ovca":
#                     O3 = O3 + KD
#
#         if KI1 == "Gubljenje":
#             H = input("Unesite tip kartice: ")
#             KD = int(("Unesite količinu: "))
#             with open(f"{I3}.txt", "a") as A:
#                 A.write("dobivanje: " + H + "" + D + "\n")
#                 if H == "Žito":
#                     Z3 = Z3 - KD
#
#                 if H == "Kamen":
#                     K3 == K3 - KD2
#                 if H == "Drvo":
#                     D3 == D3 - KD
#
#                 if H == "Cigla":
#                     C3 = C3 - KD
#
#                 if H == "Ovca":
#                     O3 = O3 - KD
#
#
#     if II1 == 1:
#         player4()
#
#     if B3 >= 12:
#         exit(f"{I3} je pobjedio")
#
#
# def player4():
#     II1 = 0
#     while II1 == 0:
#         KI1 = input("Unesite komandu: ")
#         if KI1 == "Aktivacija Kartice Razvoja":
#             aktivacija_kartice_razvoja()
#
#         if KI1 == "Sljedeći igrač":
#             II1 = 1
#
#         if KI1 == "Kupnja Kartice Razvoja":
#             kartica_razvoja()
#
#         if KI1 == "Gradnja":
#             gradnja()
#
#         if KI1 == "Nagrada":
#             Nagrade()
#
#         if KI1 == "Dobivanje":
#
#             H = input("Unesite tip kartice: ")
#             KD = int(("Unesite količinu: "))
#             with open(f"{I4}.txt", "a") as A:
#                 A.write("dobivanje: " + H + "" + D + "\n")
#                 if H == "Žito":
#                     Z4 = Z4 + KD
#
#                 if H == "Kamen":
#                     K4 == K4 + KD
#
#                 if H == "Drvo":
#                     D4 == D4 + KD
#
#                 if H == "Cigla":
#                     C4 = C4 + KD
#
#                 if H == "Ovca":
#                     O4 = O4 + KD
#
#         if KI1 == "Gubljenje":
#             H = input("Unesite tip kartice: ")
#             KD = int(("Unesite količinu: "))
#             with open(f"{I4}.txt", "a") as A:
#                 A.write("dobivanje: " + H + "" + D + "\n")
#                 if H == "Žito":
#                     Z4 = Z4 - KD
#
#                 if H == "Kamen":
#                     K4 == K4 - KD2
#                 if H == "Drvo":
#                     D4 == D4 - KD
#
#                 if H == "Cigla":
#                     C4 = C4 - KD
#
#                 if H == "Ovca":
#                     O4 = O4 - KD
#
#     if II1 == 1:
#         player1()
#
#     if B4 >= 12:
#         exit(f"{I4} je pobjedio")
#
#
#
#
# #player1()
def igrac1(Z1, K1, O1, D1, C1):
    print("Sada je na redu: ",I1)
    A = input("Unesite komandu")


































