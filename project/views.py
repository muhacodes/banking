from django.shortcuts import render,HttpResponseRedirect
from Clients.models import Client
from django.urls import reverse
from django.contrib import messages
from django.db.models import Sum

# Create your views here.

def home(request):
    context = {
        'clients' : Client.objects.count(),
        'cash' : Client.objects.aggregate(Sum('amount'))['amount__sum']
    }

    return render(request, 'home.html', context)
