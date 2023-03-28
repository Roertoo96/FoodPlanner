import os
import openai
import re
from FoodGenerator.views import *



def askgpt(suche_filter, vorauswahl_filter, portionen):

# Ersetzen Sie 'your_api_key' durch Ihren tatsächlichen API-Schlüssel.
    openai.api_key = os.environ['OPENAI_API_KEY']

    # System- und Benutzerrollen mit Anweisungen und Anfrage
    system_intel = "Du bist GPT-4, ein hochintelligentes KI-Sprachmodell. Stelle dem Benutzer ein Rezept im angegebenen JSON-Format zur Verfügung."
    jsonvorlage = """
    {
    "title": "",
    "ingredients": [],
    "instructions": [],
    "servings": "",
    "prep_time": "",
    "cook_time": ""
    }
    """
    prompt = f"""Gib mir ein Rezept mit folgende Kriterien: {vorauswahl_filter}, {suche_filter}, {portionen} Personen. Gebe es in folgendem JSON-Format aus: {jsonvorlage}"""

    # Funktion, die die GPT-4 API aufruft
    def ask_GPT4(system_intel, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_intel},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1200
        )
        
        return response.choices[0].message.content

    # Aufrufen der Funktion und Speichern der Antwort
    recipe_json_text = ask_GPT4(system_intel, prompt)

    # Laden der Antwort als JSON-Objekt
    rezept = json.loads(recipe_json_text)

    # Ausgabe des Rezepts im JSON-Format
    print(json.dumps(rezept, indent=2, ensure_ascii=False))

    return rezept







