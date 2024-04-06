# Python program to write JSON
# to a file
var1 = input("Unesite ime knjige: ")
var2 = input("Unesite ime autora: ")
var3 = input("Unesite id žanra: ")
var4 = input("Unesite ID knjige: ")

import json

# Data to be written
dictionary = {
    "Ime knjige": var1,
    "Autor": var2,
    "Id Zanra": var3,
    "ID": var4
}

with open(f"{var1}.json", "w") as outfile:
    json.dump(dictionary, outfile)
