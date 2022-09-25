from django.shortcuts import render,redirect
from .forms import DataCollection
from .models import Login
from django.db.models import Count
import datetime
# Create your views here.

def another_page(request):
    return render(request,'HTML/another.html')

def coockie_details(request):
    form = Login()
    if request.method == 'POST':
        form = DataCollection(request.POST)
        if form.is_valid():
            form.save()
        return listUsers(request)
    total = Login.objects.all().annotate(Count('updated_at'))
    usersDict = {'users':form,'count':len(total)}
    return render(request,'HTML/display.html',usersDict)

def listUsers(request):
    users = Login.objects.all()
    count = Login.objects.all().annotate(Count('updated_at'))
    usersDict = {'users':users,"count":count}
    return render(request,'HTML/all.html',usersDict)
