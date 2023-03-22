from python_bring_api.bring import Bring
import os
from FoodGenerator.views import *

BRINGUSER = os.environ['BRINGACC']
BRINGPW = os.environ['BRINGPW']

#Create Bring instance with email and password
bring = Bring(BRINGUSER, BRINGPW)
# Login
bring.login()

lists = bring.loadLists()

# Wähle die erste Liste aus der Liste der verfügbaren Listen
list_uuid = lists['lists'][0]['listUuid']

def additem(Zutaten):
    print('Test_______________')
    print(Zutaten)
    for i in Zutaten:
        print(i)
        bring.saveItem(lists['lists'][0]['listUuid'], i)

    return




# Hole alle Artikel der ausgewählten Liste
# items = bring.getItems(list_uuid)

# Gib alle Artikel aus
# for item in items['purchase']:
#     print(item['name'])
# Save an item with specifications to a certain shopping list




