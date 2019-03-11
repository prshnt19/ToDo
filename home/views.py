from django.shortcuts import render
from .models import ToDo
from django.http import HttpResponseRedirect, JsonResponse
from .tasks import send_email


def todo(request):
    due = ToDo.objects.all().filter(status="due")
    done = ToDo.objects.all().filter(status="done")
    overdue = ToDo.objects.all().filter(status='overdue')
    return render(request, 'index.html', {'overdue': overdue, 'done': done, 'due': due})


def add(request):
    return render(request, 'add.html')


def addtask(request):
    task = request.POST.get('task')
    date = request.POST.get('date')
    time = request.POST.get('time')
    priority = request.POST.get('priority')
    category = request.POST.get('category')
    todo = ToDo.objects.create(task=task, date=date, time=time, priority=priority, category=category, status="due")
    send_email.delay(todo.id)
    return HttpResponseRedirect('/')


def done(request, id):
    don = ToDo.objects.get(id=id)
    don.status = "done"
    don.save()
    return HttpResponseRedirect('/')


def edit(request, id):
    return HttpResponseRedirect('/')


def delete(request, id):
    ToDo.objects.get(id=id).delete()
    return HttpResponseRedirect('/')


def add_name(request):
    name = request.POST.get('name')
    data = {'name': name}
    return JsonResponse(data)


def add_number(request):
    number = request.POST.get('number')
    data = {'number': number}
    return JsonResponse(data)
