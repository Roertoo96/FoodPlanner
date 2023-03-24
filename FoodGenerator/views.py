from django.shortcuts import render
import json
from FoodGenerator.gpt import askgpt
from FoodGenerator.bring import additem
from FoodGenerator.mongo import addlastsearch
from FoodGenerator.mongo import downloadlastadd
from FoodGenerator.mongo import downloadrecipe
from FoodGenerator.mongo import changecollection
import os
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.contrib.auth import logout
from django.views.generic import RedirectView

class CustomLogoutView(LogoutView):
    template_name = 'logout.html'
    success_url = reverse_lazy('')

    def get(self, request, *args, **kwargs):
        if request.GET.get('confirm', False):
            return super().get(request, *args, **kwargs)
        return render(request, self.template_name)



@login_required
def profile(request):
    return render(request, 'profile.html')

class CustomLogoutView(RedirectView):
    url = reverse_lazy('food')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('food')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('food')
        else:
            #invalid credentials
            pass
    else:
        return render(request, 'login.html')

# Create your views here.
def kalender(request):
    return render(request,'kalender.html')




def food(request):

    lastrecipe = downloadlastadd()
    print(lastrecipe)




    #print(lastrecipe)
    if 'query' in request.POST:
        def get_querydict_values():
            querydict = request.POST
            suche_filter = querydict.get('query', [''])
            vorauswahl_filter = querydict.get('filters', [''])
            return suche_filter, vorauswahl_filter, querydict
        suche_filter, vorauswahl_filter, querydict = get_querydict_values ()
        rezept,name,ingredients,instructions = askgpt(suche_filter, vorauswahl_filter)
        erg = addlastsearch(rezept,name,ingredients,instructions,vorauswahl_filter,suche_filter)
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


    if "saveinbook" in request.POST:
        print(request.POST)
        rezeptsaveinbook = request.POST["saveinbook"]
        print(rezeptsaveinbook)

        changecollection(rezeptsaveinbook)





    
    else:
        print('Fehler')
        #print(request.POST)

    
    context = {
        'lastrecipe': lastrecipe,

    }


    return render(request,'food.html', context)

@login_required
def book(request):
    allrecipe = downloadrecipe()

    context = {
        'allrecipe': allrecipe,
    }


    return render(request,'Rezeptbuch.html', context)