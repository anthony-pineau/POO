class WordGuesser():

    def __init__(self):
         self._mots = []
         self._motsUpper = []
         self._motsLower = []
         self._motsCapitalize = []
         self._motsSansAccent = []
         self._listeMots = []
         self._l33t = []

    # getter method mots
    def get_mots(self):
        return self._mots
      
    # setter method mots
    def set_mots(self, x):
        self._mots.append(x)
    
    # getter method motsUpper
    def get_motsUpper(self):
        return self._motsUpper
      
    # setter method motsUpper
    def set_motsUpper(self, x):
        self._motsUpper.append(x)

    # getter method motsLower
    def get_motsLower(self):
        return self._motsLower
      
    # setter method motsLower
    def set_motsLower(self, x):
        self._motsLower.append(x)

    # getter method motsCapitalize
    def get_motsCapitalize(self):
        return self._motsCapitalize
      
    # setter method motsCapitalize
    def set_motsCapitalize(self, x):
        self._motsCapitalize.append(x)
    
    # getter method motsSansAccent
    def get_motsSansAccent(self):
        return self._motsSansAccent
      
    # setter method motsSansAccent
    def set_motsSansAccent(self, x):
        self._motsSansAccent.append(x)
    
    # getter method listeMots
    def get_listeMots(self):
        return self._listeMots
      
    # setter method listeMots
    def set_listeMots(self, x):
        self._listeMots.append(x)

    # getter method l33t
    def get_l33t(self):
        return self._l33t
      
    # setter method l33t
    def set_l33t(self, x):
        self._l33t.append(x)
      
guesser = WordGuesser()

guesser.set_mots("téèèst")
guesser.set_mots("WayToLearnX")

name = str(input("Entrer un mot"))
guesser.set_mots(name)

mots = guesser.get_mots()

for i in mots:
    guesser.set_motsUpper(i.upper())

for i in mots:
    guesser.set_motsLower(i.lower())

for i in mots:
    guesser.set_motsCapitalize(i.capitalize())

# Remplacer les accents
for ligne in mots:
    accent = ['é', 'è', 'ê', 'à', 'ù', 'û', 'ç', 'ô', 'î', 'ï', 'â']
    sans_accent = ['e', 'e', 'e', 'a', 'u', 'u', 'c', 'o', 'i', 'i', 'a']
    i = 0
    while i < len(accent):
        ligne = ligne.replace(accent[i], sans_accent[i])
        i += 1
    guesser.set_motsSansAccent(ligne)

# L33t
for ligne in mots:
    caratere = ['4', '3', '1', '0', '1', '5', '8', '7', '2', '6']
    caracteresSpeciaux = ['a', 'e', 'i', 'o', 'l', 's', 'b', 't', 'z', 'g']
    i = 0
    while i < len(caratere):
        ligne = ligne.replace(caratere[i], caracteresSpeciaux[i])
        i += 1
    guesser.set_l33t(ligne)

strListeWord = []
strListeWord += guesser.get_motsLower()
strListeWord += guesser.get_motsSansAccent()
strListeWord += guesser.get_motsUpper()
strListeWord += guesser.get_motsCapitalize()
strListeWord += guesser.get_l33t()

guesser.set_listeMots(strListeWord)