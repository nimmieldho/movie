from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Movie
from . forms import movieform
# Create your views here.
def index(request):
    obj=Movie.objects.all()
    return render(request,"index.html",{'obj1':obj})
def detail(request,movieid):
    movie=Movie.objects.get(id=movieid)
    return render(request,"detail.html",{'movies':movie})

def add(request):
    if request.method=='POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        image = request.FILES['image']
        movie = Movie(name=name,desc=desc, year=year,image=image)
        movie.save()
    return render(request,"add.html")

def update(request,id):
    movie = Movie.objects.get(id=id)
    forms = movieform(request.POST or None,request.FILES,instance=movie)
    if forms . is_valid():
        forms.save()
        return redirect('/')
    return render(request,"edit.html",{'movie':movie,'forms':forms})


def delete(request,id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,"delete.html")



