import os
import openai
import re
from FoodGenerator.views import *


######gpt4#########
# def askgpt(suche_filter, vorauswahl_filter, portionen):

# # Ersetzen Sie 'your_api_key' durch Ihren tatsächlichen API-Schlüssel.
#     openai.api_key = os.environ['OPENAI_API_KEY']

#     # System- und Benutzerrollen mit Anweisungen und Anfrage
#     system_intel = "Du bist GPT-4, ein hochintelligentes KI-Sprachmodell. Stelle dem Benutzer ein Rezept im angegebenen JSON-Format zur Verfügung."
#     jsonvorlage = """
#     {
#     "title": "",
#     "ingredients": [],
#     "instructions": [],
#     "Inhaltsstoffe": [
#     "Protein": "",
#     "Kohlenhydrate": "",
#     "Fette": "",
#     "Ballaststoffe": ""
#     ],
#     "servings": "",
#     "prep_time": "",
#     "cook_time": ""
#     }
#     """
#     prompt = f"""Gib mir ein Rezept mit folgende Kriterien: {vorauswahl_filter}, {suche_filter}, {portionen} Personen.Schätze folgende Inhaltsstoffe mit Gering, Mittel, Viel: Protien, Kohlenhydrate, Fette, Ballaststoffe. Gebe es in folgendem JSON-Format aus: {jsonvorlage}"""

#     # Funktion, die die GPT-4 API aufruft
#     def ask_GPT4(system_intel, prompt):
#         response = openai.ChatCompletion.create(
#             model="gpt-4",
#             messages=[
#                 {"role": "system", "content": system_intel},
#                 {"role": "user", "content": prompt}
#             ],
#             max_tokens=1200
#         )
        
#         return response.choices[0].message.content

#     # Aufrufen der Funktion und Speichern der Antwort
#     recipe_json_text = ask_GPT4(system_intel, prompt)

#     # Laden der Antwort als JSON-Objekt
#     rezept = json.loads(recipe_json_text)

#     # Ausgabe des Rezepts im JSON-Format
#     print(json.dumps(rezept, indent=2, ensure_ascii=False))

#     return rezept


#########GTP3#######
def askgpt(suche_filter, vorauswahl_filter, portionen):

# Ersetzen Sie 'your_api_key' durch Ihren tatsächlichen API-Schlüssel.
    openai.api_key = os.environ['OPENAI_API_KEY']


    # System- und Benutzerrollen mit Anweisungen und Anfrage
    system_intel = "Achte darauf das du nur das geforderte JSON Format ausgibst"
    jsonvorlage = """
        {
        "title": "",
        "ingredients": [],
        "instructions": [],
        "Inhaltsstoffe": [
        "Protein": "",
        "Kohlenhydrate": "",
        "Fette": "",
        "Ballaststoffe": ""
        ],
        "servings": "",
        "prep_time": "",
        "cook_time": ""
        }
        """

    if not vorauswahl_filter and not suche_filter:
        print("leer")
        
        prompt = f"""Erstelle mir ein zufälliges Rezept für {portionen} Personen. Schätze folgende Inhaltsstoffe mit Gering, Mittel, Viel: Protien, Kohlenhydrate, Fette, Ballaststoffe. Gebe das rezept nur in folgendem JSON Format wieder: {jsonvorlage}"""
        
    else:
        prompt = f"""Gib mir ein Rezept mit folgende Kriterien: {vorauswahl_filter}, {suche_filter}, {portionen} Personen.Schätze folgende Inhaltsstoffe mit Gering, Mittel, Viel: Protien, Kohlenhydrate, Fette, Ballaststoffe. Gebe das rezept nur in folgendem JSON Format wieder: {jsonvorlage}"""


    # Funktion, die die GPT-4 API aufruft
    def ask_GPT4(system_intel, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_intel},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1200
        )
            
        return response.choices[0].message.content

    # Aufrufen der Funktion und Speichern der Antwort
    recipe_json_text = ask_GPT4(system_intel, prompt)
    print(recipe_json_text)


    start_position = recipe_json_text.find("{")
    end_position = recipe_json_text.rfind("}")

    if start_position != -1 and end_position != -1 and end_position > start_position:
        filtered_text = recipe_json_text[start_position:end_position + 1]
    else:
        filtered_text = ""

    print(filtered_text)


        #Laden der Antwort als JSON-Objekt
    rezept = json.loads(filtered_text)

        # Ausgabe des Rezepts im JSON-Format
        #print(json.dumps(rezept, indent=2, ensure_ascii=False))

    return rezept




