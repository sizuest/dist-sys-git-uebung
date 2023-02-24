from person import Person

# ANPASSEN
# ===============================================
person = Person("Bucher", "Leandro")
# Optional / zum auskommentieren
person.set_dialekt("Lozaernerduetsch")
person.set_haustier("Chatze ond Scheldkrote")
person.set_lieblingsfarbe("Blau")
person.set_Brille(True)
# ===============================================
person.toJSON("data/"+person.vorname.lower()+"."+person.name.lower())