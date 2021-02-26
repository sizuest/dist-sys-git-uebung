from person import Person

# ANPASSEN
# ===============================================
person = Person("Mezenen", "Kenny")

# Optional / zum auskommentieren
# person.set_dialekt("Zuerich")
# person.set_haustier("Haustier")
# person.set_lieblingsfarbe("Schwarz")

# ===============================================
person.toJSON("data/"+person.vorname.lower()+"."+person.name.lower())