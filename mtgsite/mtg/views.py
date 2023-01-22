from django.shortcuts import render
from mtg.models import Cards

def card_index(request):
    cards = Cards.objects.all()
    context = {
        'cards': cards
    }
    return render(request, 'card_index.html', context)

def card_detail(request, pk):
    card = Cards.objects.get(pk=pk)
    context = {
        'card': card
    }
    return render(request, 'card_detail.html', context)