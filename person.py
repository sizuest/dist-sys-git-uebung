import json


class Person:
    lieblingsfarbe = ""
    mag_bier = None

    def __init__(self, name, vorname):
        self.name = name
        self.vorname = vorname

    def set_lieblingsfarbe(self, lieblingsfarbe):
        self.lieblingsfarbe = lieblingsfarbe

    def set_mag_bier(self, mag_bier):
        self.mag_bier = mag_bier

    def to_string(self):
        out = self.name + ", " + self.vorname

        if self.lieblingsfarbe != "":
            out += "\n\tLieblingsfarbe: " + self.lieblingsfarbe

        if self.mag_bier is not None:
            if self.mag_bier:
                out += "\n\tMag Bier"
            else:
                out += "\n\tMag kein Bier"

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
