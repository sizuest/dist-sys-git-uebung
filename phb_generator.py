from person import Person
# ANPASSEN # ===============================================
person = Person("Bachmann", "Philipp")
# Optional / zum auskommentieren
person.set_dialekt("Lozerner")
person.set_haustier("Staffordshire Bullterrier: Lenny")
person.set_lieblingsfarbe("Dunkelblau")
person.set_brille("Ja")
person.set_autofahrer("Ja")
# ===============================================
person.toJSON("data/"+person.vorname.lower()+"."+person.name.lower())
