from service import unos_imena_igraca as igraci
from service import kreiranje_datoteka as datoteke
from service import gradnja as gradnja
from service import kartica_razvoja as kartica_razvoja
from service import aktivacija_kartice_razvoja as aktivacija
from service import Nagrade as nagrade
from service import player1 as igrac1
from service import player3 as igrac3
from service import player4 as igrac4


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    I1, I2, I3, I4, I5 = igraci()
    print(I1, I2, I3, I4, I5)
    datoteke(I1, I2, I3, I4, I5)
    igrac1()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
