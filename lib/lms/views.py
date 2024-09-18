from django.shortcuts import render ,redirect
from .models import Student,Book
from django.db.models import Q

# Create your views here.

def index(request):

    return render(request,'index.html')

def student (request):
    data ={}
    data['students'] = Student.objects.all()
    return render(request,'student.html',data)
   
def deletestudent(request, id):
    student= Student.objects.get(id= id)
    student.delete()
    return redirect(deletestudent)

def search (request):
    data={}
    search = request.GET.get('search')
    query = (Q(name__icontains=search)|Q(fathername__icontains=search)|Q(mothername__icontains=search))
    data['students'] = Student.objects.filter(query)
    return render(request,"student.html",data)


def book (request):
    dol ={}
    dol['books'] = Book.objects.all()
    return render(request,'book.html',dol)
def deletebook(request, id):
    book= Book.objects.get(id= id)
    book.delete()
    return redirect(deletebook)