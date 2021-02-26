from person import Person

# ANPASSEN
# ===============================================
person = Person("Test", "Meier")

# Optional / zum auskommentieren
person.set_dialekt("Äntlibuech")
person.set_haustier("kein")
person.set_lieblingsfarbe("türkis")
person.set_haar_farbe("Rot")
person.set_studiengang("WI")

# ===============================================
person.toJSON("data/"+person.vorname.lower()+"."+person.name.lower())