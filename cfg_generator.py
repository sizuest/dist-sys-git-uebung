from person import Person

# ANPASSEN
# ===============================================

person = Person("Rogenmoser", "Yves")

# Optional / zum auskommentieren
person.set_dialekt("Zuger")
person.set_haustier("Katze")
person.set_lieblingsfarbe("Blue")


# ===============================================
person.toJSON("data/"+person.vorname.lower()+"."+person.name.lower())