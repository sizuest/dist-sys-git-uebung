import json


class Person:
    lieblingsfarbe = ""
    haustier = ""
    dialekt = ""
    brille = False
    handymarke = ""


    def __init__(self, name, vorname):
        self.name = name
        self.vorname = vorname

    def set_lieblingsfarbe(self, lieblingsfarbe):
        self.lieblingsfarbe = lieblingsfarbe

    def set_haustier(self, haustier):
        self.haustier = haustier

    def set_dialekt(self, dialekt):
        self.dialekt = dialekt

    def set_Brille(self, brille):
        self.brille = brille

<<<<<<< HEAD
    def set_alter(self, alter):
        self.alter = alter
=======
    def set_handymarke(self, marke):
        self.handymarke = marke

>>>>>>> f233f8beb8c8ef719a84f8f5dad2cdc5a1fcc1b5

    def to_string(self):
        out = self.name +", "+self.vorname

        if self.lieblingsfarbe != "":
            out += "\n\tLieblingsfarbe: "+self.lieblingsfarbe

        if self.haustier != "":
            out += "\n\tHaustier: "+self.haustier

        if self.dialekt != "":
            out += "\n\tDialekt: "+self.dialekt

        if self.brille:
            out += "\n\tBrillenträger:in"

        if self.alter:
            out += "\n\tAlter: "+self.alter

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