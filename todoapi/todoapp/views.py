from rest_framework import viewsets
from .models import TODO
from .serializers import TODOSerializer
from django.shortcuts import render,redirect
from .models import TODO
from .forms import TodoForm


class TODOViewset(viewsets.ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOSerializer


def index(request):
    task = TODO.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title','')
        description = request.POST.get('description','')
        date = request.POST.get('date','')

        task =TODO(title=title,description=description,date=date)
        task.save()
        return redirect('/index')

    return render(request,'todoapp/index.html',{'task':task})

def date(request):
    if request.method == 'GET':
        date_search = request.GET.get('date_search')
        task = TODO.objects.all().filter(date=date_search)

    return render(request,'todoapp/date.html',{'task':task})


def deletetask(request,taskid):
    task = TODO.objects.get(id=taskid)

    if request.method =='POST':
        task.delete()
        return redirect('/index')

    return render(request,'todoapp/delete1.html',{'task':task})

def update(request,id):
    task = TODO.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/index')
    return render(request,'todoapp/edit.html',{'form':form, 'task':task})

