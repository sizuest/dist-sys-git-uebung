from person import Person

# ANPASSEN
# ===============================================
person = Person("Züst", "Simon")


# Optional / zum auskommentieren
person.set_dialekt("ZH-Oberland")
person.set_haustier("Katzen")
person.set_haar_farbe("Schwarz")
person.set_studiengang("MSc ME")


# ===============================================
person.toJSON("data/"+person.vorname.lower()+"."+person.name.lower())