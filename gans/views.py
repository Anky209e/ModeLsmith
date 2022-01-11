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