from pymongo import MongoClient
from datetime import datetime
from FoodGenerator.views import *
import os


MONGOUSER = os.environ['MONGOUSER']
MONGOPW = os.environ['MONGOPW']
MONGOSERVER = os.environ['MONGOSERVER']



client = MongoClient(f"mongodb+srv://{MONGOUSER}:{MONGOPW}@{MONGOSERVER}/?retryWrites=true&w=majority")

db = client.get_database('rezepte_db')
records = db.rezepte_lastsearch
recordsrecipe = db.rezepte_records


def addlastsearch(rezept,name,ingredients,instructions,vorauswahl_filter,suche_filter):

    uploaddoc = {
        'rezept': name,
        'Zutaten': ingredients,
        'Beschreibung': instructions,
        'tags' : vorauswahl_filter + suche_filter,

    }
    records.insert_one(uploaddoc)
    
    return

def downloadlastadd():
    #print("in Download")
    documents = records.find().sort('date', 1).limit(3);
    #print(documents)
    rezepte = []
    for document in documents:
        print(document)
        rezept_dict = {}
        rezept_dict['rezept'] = document['rezept']
        rezept_dict['zutaten'] = document['Zutaten']
        rezept_dict['Beschreibung'] = document['Beschreibung']
        #rezept_dict['tag'] = document['tag']
        rezepte.append(rezept_dict)
        
    return rezepte

def downloadrecipe():
    #print("in Download Rezepte")
    documents = recordsrecipe.find()
    #print(documents)
    recipearry = []
    for document in documents:
        #print(document)
        
        rezept_dict = {}
        rezept_dict['rezept'] = document['rezept']
        rezept_dict['zutaten'] = document['Zutaten']
        rezept_dict['Beschreibung'] = document['Beschreibung']
        rezept_dict['tags'] = document['tags']
        recipearry.append(rezept_dict)
        
    return recipearry


def changecollection(rezeptsaveinbook):
    document_to_move = records.find_one({"rezept": rezeptsaveinbook})
    recordsrecipe.insert_one(document_to_move)
    records.delete_one({"rezept": rezeptsaveinbook})
    return
    
    






#find
#all = list(records.find({'name': 'Nudeln'}))
#print(all)
#create

# newdoc = {
#     'name': 'Nudeln',
#     'beschreibung': 'Nudeln mit Peste',
#     'Zutat 1' : 'Nudeln',
#     'Zutat 2' : 'Pesto',
# }

# records.insert_one(newdoc)
