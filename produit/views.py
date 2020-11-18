from django.shortcuts import render
from django.http import HttpResponse
from commande.models import Commande
from client.models import Client

# Create your views here.
def home(request):
    commande=Commande.objects.all()
    client=Client.objects.all()
    context={'commande':commande,'client':client}
    return render(request,'produit/acceuil.html',context)
