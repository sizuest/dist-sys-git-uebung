from person import Person

# ANPASSEN
# ===============================================
person = Person("Pascal", "Buehlmann")

# Optional / zum auskommentieren
person.set_dialekt("Äntlibuech")
person.set_haustier("kein")
person.set_lieblingsfarbe("türkis")

# ===============================================
person.toJSON("data/"+person.vorname.lower()+"."+person.name.lower())