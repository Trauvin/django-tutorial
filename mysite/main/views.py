from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item


# Create your views here.

def index(response, name):
	ls = ToDoList.objects.get(name=name) # acessando os objetos criados no shell
	items = ls.item_set.get(id=2)
	return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(ls.name, str(items.text)))
