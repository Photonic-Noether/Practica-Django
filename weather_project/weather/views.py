from django.shortcuts import render
from django.http import HttpResponse

def hola_mundo(request):
    return HttpResponse("<h1>Esto es una vista!!</h1>")
