from person import Person

# ANPASSEN
# ===============================================
person = Person("Rüttimann", "Donat")


# Optional / zum auskommentieren
person.set_dialekt("Dialekt")
person.set_haustier("Haustier")
person.set_lieblingsfarbe("Farbe")


# ===============================================
person.toJSON("data/"+person.vorname.lower()+"."+person.name.lower())