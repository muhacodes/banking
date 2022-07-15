from django.shortcuts import render,HttpResponseRedirect, HttpResponse 
from .models import Transaction
from .forms import create_form
from django.urls import reverse
from django.contrib import messages
from Clients.models import Client
from django.http import JsonResponse

# Create your views here.

def home(request):
    context = {
        'object_list' : Transaction.objects.all(),
    }

    return render(request, 'transactions.html', context)


def deposit(request):
    form = create_form(request.POST or None)

    if form.is_valid():
        instaince = form.save(commit=False)
        obj = Client.objects.get(id=instaince.client.id)
        
        if obj.amount:
            obj.amount = obj.amount + instaince.amount
            print('amount is there in client')
        else:
            obj.amount = instaince.amount
            instaince.balance = instaince.amount
            print('amount is not there in client')

        instaince.mode = "deposit"
        instaince.save()
        obj.save()
        messages.success(request, 'Your actions have been succesfully saved !')
        return HttpResponseRedirect(reverse('clients:home'))
    
    return render(request, 'deposit.html', {'form' : form} )


def withdraw(request):
    form = create_form(request.POST or None)

    if form.is_valid():
        instaince = form.save(commit=False)
        obj = Client.objects.get(id=instaince.client.id)
        obj.amount = obj.amount - instaince.amount

        instaince.mode = "withdraw"
        instaince.save()
        obj.save()
        messages.success(request, 'Your actions have been succesfully saved !')
        return HttpResponseRedirect(reverse('transactions:home'))
    
    return render(request, 'withdraw.html', {'form' : form} )


def get_amount(request, id):
    obj = Client.objects.get(id=id)
    amount = obj.amount

    return JsonResponse({'message': 'success', 'amount' : amount})