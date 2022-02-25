import json


class Person:
    lieblingsfarbe = ""
    haustier = ""
    dialekt = ""


    def __init__(self, name, vorname):
        self.name = name
        self.vorname = vorname

    def set_lieblingsfarbe(self, lieblingsfarbe):
        self.lieblingsfarbe = lieblingsfarbe

    def set_haustier(self, haustier):
        self.haustier = haustier

    def set_dialekt(self, dialekt):
        self.dialekt = dialekt

<<<<<<< HEAD
=======
    def set_Brille(self, brille):
        self.brille = brille
>>>>>>> 28d8f742dd2c5f0c804f8f5bc0eec40bb119d521

    def to_string(self):
        out = self.name +", "+self.vorname

        if self.lieblingsfarbe != "":
            out += "\n\tLieblingsfarbe: "+self.lieblingsfarbe

        if self.haustier != "":
            out += "\n\tHaustier: "+self.haustier

        if self.dialekt != "":
            out += "\n\tDialekt: "+self.dialekt

<<<<<<< HEAD
=======
        if self.brille:
            out += "\n\tBrillenträger:in"
>>>>>>> 28d8f742dd2c5f0c804f8f5bc0eec40bb119d521

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