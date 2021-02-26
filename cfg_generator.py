from person import Person

# ANPASSEN
# ===============================================
person = Person("Besic", "Amela")

# Optional / zum auskommentieren
person.set_dialekt("Luzerner")
person.set_haustier("Hund")
person.set_lieblingsfarbe("Pink")

# ===============================================
person.toJSON("data/"+person.vorname.lower()+"."+person.name.lower())