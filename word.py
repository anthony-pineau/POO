class AccentRemover():
    def remove_accents(self, word):
        accent = ['é', 'è', 'ê', 'à', 'ù', 'û', 'ç', 'ô', 'î', 'ï', 'â']
        sans_accent = ['e', 'e', 'e', 'a', 'u', 'u', 'c', 'o', 'i', 'i', 'a']
        for i in range(len(accent)):
            word = word.replace(accent[i], sans_accent[i])
        return word

class LeetConverter():
    @staticmethod
    def convert_to_leet(word):
        caracteres_speciaux = ['4', '3', '1', '0', '4', '5', '8', '7', '2', '6']
        caracteres = ['a', 'e', 'i', 'o', 'a', 's', 'b', 't', 'z', 'g']
        for i in range(len(caracteres)):
            word = word.replace(caracteres[i], caracteres_speciaux[i])
        return word

class WordGenerator():
    def __init__(self):
        self._mots = []
        self._motsUpper = []
        self._motsLower = []
        self._motsCapitalize = []
        self._motsSansAccent = []
        self._listeMots = []
        self._l33t = []

    def get_mots(self):
        return self._mots
      
    def set_mots(self, x):
        self._mots.append(x)
    
    def get_motsUpper(self):
        return self._motsUpper
      
    def set_motsUpper(self, x):
        self._motsUpper.append(x)

    def get_motsLower(self):
        return self._motsLower
      
    def set_motsLower(self, x):
        self._motsLower.append(x)

    def get_motsCapitalize(self):
        return self._motsCapitalize
      
    def set_motsCapitalize(self, x):
        self._motsCapitalize.append(x)
    
    def get_motsSansAccent(self):
        return self._motsSansAccent
      
    def set_motsSansAccent(self, x):
        self._motsSansAccent.append(x)
    
    def get_listeMots(self):
        return self._listeMots
      
    def set_listeMots(self, x):
        self._listeMots.append(x)

    def get_l33t(self):
        return self._l33t
      
    def set_l33t(self, x):
        self._l33t.append(x)

    def generate_word(self):
        mots = self.get_mots()

        for i in mots:
            self.set_motsUpper(i.upper())
 
        for i in mots:
            self.set_motsLower(i.lower())
            
        for i in mots:
            self.set_motsCapitalize(i.capitalize())

        strListeWord = []
        strListeWord.extend(self.get_mots())
        strListeWord.extend(self.get_motsLower())
        strListeWord.extend(self.get_motsUpper())
        strListeWord.extend(self.get_motsCapitalize())

        accent_remover = AccentRemover()

        for ligne in strListeWord:
            ligne = accent_remover.remove_accents(ligne)
            self.set_motsSansAccent(ligne)

        for ligne in strListeWord:
            ligne = LeetConverter.convert_to_leet(ligne)
            self.set_l33t(ligne)

        strListeWord.extend(self.get_motsSansAccent())
        strListeWord.extend(self.get_l33t())

        self.set_listeMots(list(set(strListeWord)))
