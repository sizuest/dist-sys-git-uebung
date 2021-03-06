import json


class Person:
    lieblingsfarbe = ""
    haustier = ""
    dialekt = ""
    bart = False

    studiengang= ""

    haar_farbe = ""


    def __init__(self, name, vorname):
        self.name = name
        self.vorname = vorname

    def set_lieblingsfarbe(self, lieblingsfarbe):
        self.lieblingsfarbe = lieblingsfarbe

    def set_haustier(self, haustier):
        self.haustier = haustier

    def set_dialekt(self, dialekt):
        self.dialekt = dialekt

    def set_bart(self, bart):
        self.bart = bart

    def set_studiengang(self, studiengang):
        self.studiengang = studiengang

    def set_haar_farbe(self, haar_farbe):
        self.haar_farbe = haar_farbe

    def to_string(self):
        out = self.name +", "+self.vorname

        if self.lieblingsfarbe != "":
            out += "\n\tLieblingsfarbe: "+self.lieblingsfarbe

        if self.haustier != "":
            out += "\n\tHaustier: "+self.haustier

        if self.dialekt != "":
            out += "\n\tDialekt: "+self.dialekt

        if self.bart:
            out += "\n\tHat Bart"

        if self.studiengang != "":
            out += "\n\tStudiert: "+self.studiengang

        if self.haar_farbe != "":
            out += "\n\tHaar Farbe: "+self.haar_farbe

        return out

    def toJSON(self, path):
        text_file = open(path, "w")
        text_file.write(json.dumps(self, default=lambda o: o.__dict__, indent=4))
        text_file.close()

    @staticmethod
    def fromJSON(json_file):
        cls = Person("N", "V")
        for key, value in json.load(open(json_file)).items():
            setattr(cls, key, value)
        return cls