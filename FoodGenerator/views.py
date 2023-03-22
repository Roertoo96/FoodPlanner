from django.shortcuts import render
import json
from FoodGenerator.gpt import askgpt
from FoodGenerator.bring import additem
from FoodGenerator.mongo import addlastsearch
from FoodGenerator.mongo import downloadlastadd




# Create your views here.
def food(request):

    lastrecipe = downloadlastadd()
    print(lastrecipe)



    if 'query' in request.POST:
        def get_querydict_values():
            querydict = request.POST
            suche_filter = querydict.get('query', [''])
            vorauswahl_filter = querydict.get('filters', [''])
            return suche_filter, vorauswahl_filter, querydict
        suche_filter, vorauswahl_filter, querydict = get_querydict_values ()
        rezept,name,ingredients,instructions = askgpt(suche_filter, vorauswahl_filter)
        addlastsearch(rezept,name,ingredients,instructions,vorauswahl_filter)


        context = {
        'rezept': rezept,
        'rezeptname': name,
        'Zutaten': ingredients,
        'Beschreibung': instructions,
        'lastrecipe': lastrecipe,
    }
        return render(request,'food.html', context)

    
    

    if 'saveandbuy' in request.POST:
        print("________________________________________")
        print(request.POST)
        querydict = request.POST
        Zutaten = querydict.getlist('ZutatBring', [''])
        print(Zutaten)
        additem(Zutaten)

        print("________________________________________")
    
    if 'savedata' in request.POST:
        print("________________________________________")
        print("________________________________________")
        print("________________________________________")        
        print(request.POST)
        test = request.POST.get('Beschreibung')
        print(test)

        #print(context)
        #addrezept(name,ingredients,instructions)

    
    else:
        print('___________________________')
        print('Fehler')
        print(request.POST)

    
    context = {
        'lastrecipe': lastrecipe,

    }


    return render(request,'food.html', context)