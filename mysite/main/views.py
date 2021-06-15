from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item


# Create your views here.

def index(response, id):
	ls = ToDoList.objects.get(id=id) # acessando os objetos criados no shell
	return render(response, "main/list.html", {"ls": ls})

def home(response):
	return render(response, "main/home.html", {})
