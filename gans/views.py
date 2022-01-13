from django.shortcuts import redirect, render
import random
import os
# Create your views here.
def home(request):
    models = os.listdir("./gans/classes/")
    length = len(models)

    for i in range(length):
        if models[i] == '__pycache__':
            del(models[i])
            break

    for i in range(length -1):
        models[i] = models[i][:-3]
        # models[i] = models[i].replace("_", " ")

    return render(request,"gans/home.html",{"list":models})

def abstract_art(request):
    if request.method == "POST":
        from .classes.abstract_art import save_samples
        result_pth = save_samples(1)        
        
        return render(request,"gans/abstract_art.html",{"gen":"True","img_path":result_pth, "name":"Abstract_art"})
    else:
        return render(request,"gans/abstract_art.html",{"gen":"False", "name":"Abstract Art"})



def simpson(request):
    if request.method == "POST":

        from .classes.simpson import save_samples
        
        
        result_pth = save_samples(1)
        
        
        return render(request,"gans/simpson.html",{"gen":"True","img_path":result_pth, "name":"Simpson"})
    else:
        return render(request,"gans/simpson.html",{"gen":"False", "name":"Simpson"})


def paint(request):
    if request.method == "POST":

        from .classes.paint import save_samples
        
        
        result_pth = save_samples(1)
        
        
        return render(request,"gans/paint.html",{"gen":"True","img_path":result_pth, "name":"Painter"})
    else:
        return render(request,"gans/paint.html",{"gen":"False", "name":"Painter"})


def flowers(request):
    if request.method == "POST":

        from .classes.flowers import save_samples
        
        
        result_pth = save_samples(1)
        
        
        return render(request,"gans/flowers.html",{"gen":"True","img_path":result_pth, "name":"Flower"})
    else:
        return render(request,"gans/flowers.html",{"gen":"False", "name":"Flower"})