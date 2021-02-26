from person import Person

# ANPASSEN
# ===============================================
person = Person("Rüttimann", "Donat")

Optional / zum auskommentieren
person.set_dialekt("obwaldnerdütsch")
person.set_haustier("hung")
person.set_lieblingsfarbe("grün")
person.set_bart(True)

# ===============================================
person.toJSON("data/"+person.vorname.lower()+"."+person.name.lower())