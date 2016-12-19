from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'courses_app/index.html', context)

def courses(request):
    Course.objects.create(name=request.POST['name'], description=request.POST['description'])
    course = Course.objects.all()
    return redirect('/')


def delete(request, id):
    course = Course.objects.filter(id=id)
    context = {
        'courses': course,
        'id': id
    }
    return render(request, 'courses_app/confirm.html', context)

def final_delete(request, id):
    Course.objects.filter(id=id).delete()
    return redirect('/')

def cancel(request):
    return redirect('/')