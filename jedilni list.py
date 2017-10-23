#!/usr/bin/env python
# -*- coding: utf-8 -*-
dnevni_menu = {}


print "Pozdravljeni v sistemu dnevni menu: "

while True:
    meni = raw_input("Vnesi hrano: ")
    cena_menija = raw_input("Cena menija (eur): ")
    dnevni_menu[meni] = cena_menija

    dodatni_meni = raw_input("Zelis dodati se kaksen meni (D/N)?")
    if dodatni_meni == "n":
        print "Meni: %s" %dnevni_menu

        break
"""with open (meniji, "w+") as jedilnik:
    i=0
    for task in meniji:
        print task, ":", cena[i]
        i += 1"""

with open("dnevni_menu.txt", "w+") as menu_file:
    i=0
    for dish in dnevni_menu:
        menu_file.write("%s: %s EUR\n" % (meni, dnevni_menu[meni]))
        i += 1

print "Goodbye!"
