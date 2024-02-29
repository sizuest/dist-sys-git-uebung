cfg_generator.pyfrom person import Person

# ANPASSEN
# ===============================================
person = Person("Name", "Vorname")

# Optional / zum auskommentieren
# person.set_mag_bier(True)
# person.set_lieblingsfarbe("Farbe")

# ===============================================
person.toJSON("data/"+person.vorname.lower()+"."+person.name.lower())