## 1 - Polymorphisme
Le polymorphisme en programmation orientée objet (POO) est le principe selon lequel des objets de différentes classes peuvent être traités de manière uniforme s'ils exposent une interface commune ou des méthodes avec la même signature. En Python, le polymorphisme est naturellement pris en charge grâce à sa gestion dynamique des types.

Le polymorphisme permet de traiter des objets de différentes classes de manière générique, en appelant les mêmes méthodes sur ces objets, sans se soucier de leur classe sous-jacente. Cela facilite la réutilisation du code et permet de créer des structures flexibles et extensibles.

## 2 - L'encapsulation :
L'encapsulation est une notion de la programmation orientée objet qui consiste à regrouper les données (attributs) et les méthodes qui les manipulent au sein d'une même entité, une classe en l'occurrence, et à restreindre l'accès direct aux données en les déclarant comme privées (en utilisant le préfixe "_").

Dans mon fichier [word.py](word.py) la classe WordGenerator, les attributs tels que _mots, _motsUpper, _motsLower, _motsCapitalize, _motsSansAccent, _listeMots, et _l33t sont déclarés comme privés en utilisant le préfixe _. Cela indique que ces attributs ne doivent pas être accédés directement en dehors de la classe, mais plutôt à travers les méthodes de getter et de setter fournies.

Les méthodes de getter, comme get_mots(), get_motsUpper(), get_motsLower(), etc., permettent d'accéder aux valeurs des attributs privés depuis l'extérieur de la classe. Les méthodes de setter, comme set_mots(), set_motsUpper(), set_motsLower(), etc., permettent de modifier les valeurs des attributs privés depuis l'extérieur de la classe, en les ajoutant à des listes.

## 3 - Composition

Dans le fichier [word.py](word.py) j'ai trois classes : AccentRemover, LeetConverter, et WordGenerator.

La classe AccentRemover représente un composant qui peut supprimer les accents d'un mot en utilisant la méthode remove_accents. La classe LeetConverter est également un composant qui peut convertir un mot en utilisant la méthode convert_to_leet. 

La classe WordGenerator agit comme un composite qui utilise les composants AccentRemover et LeetConverter pour générer des mots.

## 4 - Héritage

Dans le fichier [date.py](date.py) l'héritage pour créer une classe DateGenerator qui hérite de la classe DateProcessor. L'héritage permet à DateGenerator de bénéficier des fonctionnalités de DateProcessor et de les étendre selon ses besoins.

La classe DateProcessor fournit une méthode process_date qui convertit une chaîne de caractères représentant une date en un objet datetime et extrait diverses informations comme le mois, le numéro du mois, l'année et le jour. Elle retourne un dictionnaire contenant ces informations.

## 6 - Méthodes et attributs d'objets

Dans [word.py](word.py) la classes WordGenerator défini des méthodes et des attributs. 

Voici une explication des méthodes et attributs utilisés dans ces classes :

Attributs :

- _mots: Liste pour stocker les mots fournis.
- _motsUpper: Liste pour stocker les mots en majuscules.

Méthodes :

- get_mots(): Retourne la liste des mots.
- set_mots(x): Ajoute un mot à la liste des mots.

## 7 - Méthodes et attributs statiques

Les méthodes et attributs statiques sont des éléments d'une classe qui sont associés à la classe elle-même plutôt qu'à une instance spécifique de la classe.

Les méthodes statiques sont des méthodes qui peuvent être appelées directement à partir de la classe, sans avoir besoin de créer une instance de la classe. Elles sont définies à l'intérieur de la classe en utilisant le décorateur @staticmethod.

l'exemple est présent dans le fichier [word.py](word.py) la méthode `convert_to_leet` dans la classe `LeetConverter` est bien définie comme une méthode statique à l'aide du décorateur @staticmethod. Cela signifie que l'on peut l'appeler directement à partir de la classe sans avoir besoin d'instancier l'objet LeetConverter a la différence `accent_remover = AccentRemover()`. 

## 8- Méthodes et attributs de classe

Dans le fichier [date.py](date.py) les méthodes et attributs de classe :

- Méthodes de classe :

process_date(date_str): Cette méthode prend une chaîne de caractères représentant une date au format "AAAA-MM-JJ" et la convertit en un objet datetime. Elle extrait ensuite le mois, le numéro du mois, l'année et le jour à partir de cet objet et retourne un tuple contenant ces informations.

- Attributs de classe :

self._dates: Cet attribut est une liste qui stocke les dates à traiter. Il est initialisé dans le constructeur de la classe DateGenerator et peut être obtenu à l'aide de la méthode get_dates() et modifié à l'aide de la méthode set_dates(x).
self._listDate: Cet attribut est une liste qui stocke les dates traitées. Il est initialisé dans le constructeur de la classe DateGenerator et peut être obtenu à l'aide de la méthode get_listDate() et modifié à l'aide de la méthode set_listDate(x).

