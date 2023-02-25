from person import Person

# ANPASSEN
# ===============================================
person = Person("Zenklusen", "Adrian")
# Optional / zum auskommentieren
person.set_dialekt("Walliserdiitsch")
person.set_haustier("Nemo")
person.set_lieblingsfarbe("Gelb")
person.set_Brille(True)
# ===============================================
person.toJSON("data/"+person.vorname.lower()+"."+person.name.lower())