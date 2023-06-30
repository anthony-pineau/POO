import random
from flask import Flask, request, jsonify, render_template
from word import WordGenerator
from date import DateGenerator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_password', methods=['POST'])
def generate_password():
    mots = request.json['words']
    dates = request.json['dates']
    nb_mots_de_passe = int(request.json['nb_mots_de_passe'])  # Récupérer le nombre de mots de passe depuis la requête

    # Dates
    GeneratorDate = DateGenerator()

    liste_dates = []
    for date in dates:
        liste_dates += date.split(',')

    for date in liste_dates:
        GeneratorDate.set_dates(date)

    GeneratorDate.generate_date()
    dates = GeneratorDate.get_listDate()

     # Mots
    GeneratorWord = WordGenerator()
    
    liste_mots = []
    for mot in mots:
        liste_mots += mot.split(',')

    for mot in liste_mots:
        GeneratorWord.set_mots(mot)

    GeneratorWord.generate_word()
    mots = GeneratorWord.get_listeMots()

    # Fusionner les mots det dates
    fusion = []

    # Ajouter les éléments de dates au tableau fusion (convertis en texte)
    for sublist in dates:
        fusion.extend([str(item) for item in sublist])

    # Ajouter les éléments de mots au tableau fusion (convertis en texte)
    for sublist in mots:
        fusion.extend([str(item) for item in sublist])

    # Liste pour stocker les mots de passe générés
    mots_de_passe = []

    # Générer les mots de passe en combinant trois mots
    for _ in range(nb_mots_de_passe):
        random_number = random.randint(3, 5)
        mot_de_passe = ''.join(random.sample(fusion, random_number))
        mots_de_passe.append(mot_de_passe)

    return jsonify(mots_de_passe)

if __name__ == '__main__':
    app.run(debug=True)
