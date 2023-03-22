import os
import openai
import re
from FoodGenerator.views import *


def askgpt(suche_filter, vorauswahl_filter):

    # Setze die API-Schlüssel als Umgebungsvariablen
    # OPENAI_API_KEY = os.environ['OPENAIAPI']

    OPENAI_API_KEY = os.environ['OPENAI_API_KEY']

    # Konfiguriere OpenAI API-Verbindung
    openai.api_key = OPENAI_API_KEY
    #model_engine = "text-davinci-003"  # Wähle das Modell, das du verwenden möchtest
    model_engine = "text-davinci-003"

    # Definiere den Text, auf dem das Modell basieren soll
    #text = "Erstelle mir ein Gesundes Proteinreiches Rezept für 2 Personen. Liste in Stichpunkten wie es zubereitet wird"
    text = "Suche mir ein Rezept zu folgenden kreterien: " + suche_filter + ". Nutze auch folgende filter:  " +vorauswahl_filter + ". Gebe mir das Rezept in einem JSON Format mit folgenden Attributen zurück: Name, Zutaten, Zubereitung. Achte darauf das die JSON Eigenschaftsnamen immer in doppelten Anführungszeichen gesetzt sind und es keine Sinderzeichen gibt"
    print(text)
    # Rufe die Antwort vom OpenAI-Modell ab
    response = openai.Completion.create(
        engine=model_engine,
        prompt=text,
        max_tokens=850,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Gib die Antwort aus
    rezept = (response.choices[0].text.strip())
    print(rezept)

    index = rezept.find('{')
    filtered_text = rezept[index:]

    recipe = json.loads(filtered_text)
    # Extrahieren Sie die gewünschten Informationen
    name = recipe["Name"]
    ingredients = recipe["Zutaten"]
    instructions = recipe["Zubereitung"]
    # Filtern Sie die Zutaten mit Mengenangaben
    # ingredients_with_quantity = [ingredient for ingredient in ingredients if any(char.isdigit() for char in ingredient)]


    return rezept,name,ingredients,instructions








