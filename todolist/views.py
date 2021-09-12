from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.


def index(response, id):
    list = ToDoList.objects.get(id=id)
    print(list.item_set.all())
    if response.method == 'POST':
        if response.POST.get("save"):
            for item in list.item_set.all():
                if response.POST.get("c"+str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()
        elif response.POST.get("newItem"):
            text = response.POST.get("item")
            if len(text) > 2:
                list.item_set.create(text=text, complete=False)
            else:
                print("invalid")
    item = list.item_set.all()
    return render(response, "todolist/list.html", {"list": list})


def home(response):
    list = ToDoList.objects.all()
    return render(response, "todolist/home.html", {'list': list})


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data['name']
            t = ToDoList(name=n)
            t.save()
        return HttpResponseRedirect("/%i" % t.id)
    else:
        form = CreateNewList()
    return render(response, "todolist/create.html", {"form": form})
