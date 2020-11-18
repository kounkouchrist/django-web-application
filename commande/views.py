from django.shortcuts import render,HttpResponse,redirect
from produit.models import Produit
from client.models import Client
from .forms import CommandeForm
from commande.models import Commande



# Create your views here.
def List_commande(request):
    return render(request,'commande/commande.html')

def ajouter_commande(request):
    form=CommandeForm()
    if request.method=='POST':
        form=CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'commande/commande.html',context)

def modifier_commande(request,pk):
    commande=Commande.objects.get(id=pk)#obtenir la clé pk
    form=CommandeForm(instance=commande)#nous allons injecter notre commande dans le formulaire

    if request.method=='POST':
        form=CommandeForm(request.POST,instance=commande)#rajouter notre modification pour toujours garder la commande
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'commande/commande.html',context)

def supprimer_commande(request,pk):
    commande=Commande.objects.get(id=pk)
    if request.method=='POST':
        commande.delete()
        return redirect('/')
    context={'item':commande}
    return render(request,'commande/suppression.html',context)


