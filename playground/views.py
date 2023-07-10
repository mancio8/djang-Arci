from django.shortcuts import render
from django.http import HttpResponse
from .models import Partita
def say_hello(request):       
    
        
    return render(request, 'hello.html')

def savedb(request):
    if request.method=='POST':
        squadra1=request.POST['squadra1']
        squadra2=request.POST['squadra2']
        goal1=request.POST['goal1']
        goal2=request.POST['goal2']
       
        partita=Partita.objects.create(squadra1=squadra1,squadra2=squadra2,goal1=goal1, goal2=goal2)
        return render(request, 'hello.html')



