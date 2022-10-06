class Guesser():

    def __init__(self):
         self._dates = []
         self._mots =[]

    # getter method
    def get_dates(self):
        return self._dates
      
    # setter method
    def set_dates(self, x):
        self._dates = x

    # getter method
    def get_mots(self):
        return self._mots
      
    # setter method
    def set_mots(self, x):
        self._mots.append(x)

    def uppercase(x):
        x.upper() 
      
guesser = Guesser()

guesser.set_mots("test")
guesser.set_mots("WayToLearnX")

name = str(input("Entrer un mot"))
guesser.set_mots(name)

strListe = guesser.get_mots()

# https://docs.python.org/fr/3/library/datetime.html
guesser.set_dates("21/10/2022")

split = guesser.get_dates().split("/")
for key in split:
    strListe.append(key)

moisNumber = split[1]
strListe.append(split[2][2:])

mois = [{"1":"janvier",  "2":"février", "3":"mars", "4":"avril", "5":"mai", "6":"juin", "7":"juillet", "8":"août", "9":"septembre", "10":"octobre", "11":"novembre", "12":"décembre"}]

for key in mois[0]:
    if(moisNumber == key):
        strListe.append(mois[0][key])

strListe.append(guesser.get_dates())
strListe.append(guesser.get_dates().replace("/", ""))

if 'WayToLearnX' in strListe :
    print("True, 'WayToLearnX' est trouvé dans la liste : " , strListe)
