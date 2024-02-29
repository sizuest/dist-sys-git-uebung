cfg_generator.pyfrom person import Person

# ANPASSEN
# ===============================================
person = Person("Schüttler", "Dattle")

# Optional / zum auskommentieren
person.set_mag_bier(True)
# person.set_lieblingsfarbe("Farbe")

# ===============================================
person.toJSON("data/"+person.vorname.lower()+"."+person.name.lower())
