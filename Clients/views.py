from django.shortcuts import render,HttpResponseRedirect
from .models import Client
from .forms import create_form
from django.urls import reverse
from django.contrib import messages

# Create your views here.

def home(request):
    context = {
        'object_list' : Client.objects.all(),
    }

    return render(request, 'client.html', context)


def add(request):
    form = create_form(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Your actions have been succesfully saved !')
        return HttpResponseRedirect(reverse('clients:home'))
    
    return render(request, 'client-add.html', {'form' : form} )
