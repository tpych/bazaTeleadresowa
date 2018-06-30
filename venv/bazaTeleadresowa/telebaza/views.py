from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Person

# Create your views here.


def printMsg(request):
    return render(request, 'telebaza/printMsg.html')


def listPeople(request):
    people = Person.objects.all()
    return render(request, 'telebaza/listPeople.html', {'people': people})


def addPerson(request):
    banners = {'banner': 'Dodaj'}
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('surname') and request.POST.get('BirthDate') and \
         request.POST.get('phone') and request.POST.get('email'):
            try:
                person = Person()
                person.name = request.POST.get('name')
                person.surname = request.POST.get('surname')
                person.BirthDate = request.POST.get('BirthDate')
                person.phone = request.POST.get('phone')
                person.email = request.POST.get('email')
                if len(person.phone) != 9:
                    return HttpResponse("Numer telefonu ma niewlasciwa dlugosc!")
                for p in Person.objects.all():
                    if p == person:
                        return HttpResponse("Numer telefonu i adres mailowy musza byc unikalne!")
                person.save()

            except (KeyError, Person.DoesNotExist):
                return render(request, 'telebaza/addPerson.html', {'banners': banners})
            else:
                return HttpResponseRedirect(reverse('telebaza:printMsg'))
        else:
            return render(request, 'telebaza/addPerson.html', {'banners': banners})
    else:
        return render(request, 'telebaza/addPerson.html', {'banners': banners})  
