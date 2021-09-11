from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.

def index(response, id):
    list = ToDoList.objects.get(id=id)
    item = list.item_set.all()[0]
    return render(response, "todolist/list.html", {"list": list})


def home(response):
    return render(response, "todolist/home.html", {'name': "home"})
    pass


def create(response):
    form = CreateNewList()
    return render(response, "todolist/create.html", {"form": form})
