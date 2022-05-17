from django.http import HttpResponse

from .forms import MovieForm
from.models import movie
from django.shortcuts import render, redirect


# Create your views here.
def index(request):

    cenima = movie.objects.all()
    context= {
        "cenima" : cenima
    }
    return render(request,"index.html",context)
def detials(request,movie_id):
    move=movie.objects.get(id=movie_id)
    return render(request,"detial.html",{"move":move})
def add_movie(request):
    if request.method=="POST":
        name = request.POST.get("name",)
        desc = request.POST.get("desc", )
        year = request.POST.get("year", )
        img = request.FILES['img']
        move=movie(name=name,desc=desc,year=year,img=img)
        move.save()
        return redirect('/')
    return  render(request,'add.html')
def update(request,id):
    move=movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=move)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form':form,'move':move})
def delete(request,id):
    if request.method == "POST":
        move=movie.objects.get(id=id)
        move.delete()
        return redirect('/')
    return render(request,'delete.html')