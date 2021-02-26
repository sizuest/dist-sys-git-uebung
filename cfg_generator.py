from person import Person

# ANPASSEN
# ===============================================
<<<<<<< HEAD
person = Person("Besic", "Amela")

# Optional / zum auskommentieren
person.set_dialekt("Luzerner")
person.set_haustier("Hund")
person.set_lieblingsfarbe("Pink")
=======

person = Person("Rogenmoser", "Yves")

# Optional / zum auskommentieren
person.set_dialekt("Zuger")
person.set_haustier("Katze")
person.set_lieblingsfarbe("Blue")

>>>>>>> b937c57a182a0a3f3e9deaaffc1211fe241e0a87

# ===============================================
person.toJSON("data/"+person.vorname.lower()+"."+person.name.lower())