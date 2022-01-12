from django.shortcuts import redirect, render
import random
import os
# Create your views here.
def home(request):
    return render(request,"gans/home.html")
def abs_art(request):
    if request.method == "POST":

        from .classes.abs_art import save_samples
        
        
        result_pth = save_samples(1)
        
        
        return render(request,"gans/abs_art.html",{"gen":"True","img_path":result_pth})
    else:
        return render(request,"gans/abs_art.html",{"gen":"False"})



def simpson(request):
    if request.method == "POST":

        from .classes.simpson import save_samples
        
        
        result_pth = save_samples(1)
        
        
        return render(request,"gans/simpson.html",{"gen":"True","img_path":result_pth})
    else:
        return render(request,"gans/simpson.html",{"gen":"False"})


def paint(request):
    if request.method == "POST":

        from .classes.paint import save_samples
        
        
        result_pth = save_samples(1)
        
        
        return render(request,"gans/paint.html",{"gen":"True","img_path":result_pth})
    else:
        return render(request,"gans/paint.html",{"gen":"False"})


def flowers(request):
    if request.method == "POST":

        from .classes.flowers import save_samples
        
        
        result_pth = save_samples(1)
        
        
        return render(request,"gans/flowers.html",{"gen":"True","img_path":result_pth})
    else:
        return render(request,"gans/flowers.html",{"gen":"False"})