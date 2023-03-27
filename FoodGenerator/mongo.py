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


def addlastsearch(rezept,name,ingredients,instructions,vorauswahl_filter,suche_filter,user):

    uploaddoc = {
        'rezept': name,
        'Zutaten': ingredients,
        'Beschreibung': instructions,
        'tags' : vorauswahl_filter + suche_filter,
        'user' : user,

    }
    records.insert_one(uploaddoc)
    
    return

def downloadlastadd(user):
    #print("in Download")
    userquery = {"user":user}
    documents = records.find(userquery)
    #print("_____________________________________")
    #print(documents)
    docsort = documents.sort('date', 1).limit(3);
    #print("_______________________")
    #print(docsort)
    #print(documents)
    rezepte = []
    for document in docsort:
        #print("1__________________")
        #print(document)
        #print("2__________________")
        rezept_dict = {}
        rezept_dict['rezept'] = document['rezept']
        rezept_dict['zutaten'] = document['Zutaten']
        rezept_dict['Beschreibung'] = document['Beschreibung']
        #rezept_dict['tag'] = document['tag']
        rezepte.append(rezept_dict)
    #print(rezepte)
        
    return rezepte

def downloadrecipe(user):
    #print("in Download Rezepte")
    userquery = {"user":user}
    documents = recordsrecipe.find(userquery)
    print(documents)
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
