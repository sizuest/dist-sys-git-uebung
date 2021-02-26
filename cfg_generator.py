from person import Person

# ANPASSEN
# ===============================================
person = Person("Name", "Vorname")

# Optional / zum auskommentieren
person.set_dialekt("Dialekt")
person.set_haustier("Haustier")
person.set_lieblingsfarbe("Farbe")

# ===============================================
person.toJSON("data/"+person.vorname.lower()+"."+person.name.lower())