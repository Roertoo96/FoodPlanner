from django.shortcuts import render
import json
from FoodGenerator.gpt import askgpt
from FoodGenerator.bring import additem
from FoodGenerator.mongo import addlastsearch
from FoodGenerator.mongo import downloadlastadd
from FoodGenerator.mongo import downloadrecipe
import os




# Create your views here.
def food(request):

    lastrecipe = downloadlastadd()




    #print(lastrecipe)
    if 'query' in request.POST:
        def get_querydict_values():
            querydict = request.POST
            suche_filter = querydict.get('query', [''])
            vorauswahl_filter = querydict.get('filters', [''])
            return suche_filter, vorauswahl_filter, querydict
        suche_filter, vorauswahl_filter, querydict = get_querydict_values ()
        rezept,name,ingredients,instructions = askgpt(suche_filter, vorauswahl_filter)
        erg = addlastsearch(rezept,name,ingredients,instructions,vorauswahl_filter)
        #print(erg)
        context = {
        'rezept': rezept,
        'rezeptname': name,
        'Zutaten': ingredients,
        'Beschreibung': instructions,
        'lastrecipe': lastrecipe,
    }
        return render(request,'food.html', context)

    if 'saveandbuy' in request.POST:

        querydict = request.POST
        Zutaten = querydict.getlist('ZutatBring', [''])
        additem(Zutaten)

    
    if 'savedata' in request.POST:     
        test = request.POST.get('Beschreibung')

    if 'savedatainbook' in request.POST:
        print(request.POST)
    
    else:
        print('Fehler')
        #print(request.POST)

    
    context = {
        'lastrecipe': lastrecipe,

    }


    return render(request,'food.html', context)


def book(request):
    allrecipe = downloadrecipe()

    context = {
        'allrecipe': allrecipe,
    }


    return render(request,'Rezeptbuch.html', context)