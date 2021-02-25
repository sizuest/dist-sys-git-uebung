from person import Person
import os


if __name__ == '__main__':
    for file in os.listdir("data"):
        try:
            print(Person.fromJSON("data/"+file).to_string())
        except:
            print('Fehler in Datei "'+file+'"')

