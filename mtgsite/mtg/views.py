from django.shortcuts import render

def index(request):
    return render(request, 'mtg/index.html', {})

def decks(request):
    return render(request, 'mtg/decks.html', {})