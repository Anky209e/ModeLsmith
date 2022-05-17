from django.shortcuts import redirect, render
import random
import os
# Create your views here.
def home(request):
    models = os.listdir("./gans/classes/")
    
    if "__pycache__" in models:
        models.remove("__pycache__")

    for i in range(len(models)):
        models[i] = models[i][:-3]

    return render(request,"gans/home.html",{"list":models})

def abstract_art(request):
    if request.method == "POST":
        from .classes.abstract_art import save_samples
        result_pth = save_samples(4)        
        
        return render(request,"gans/abstract_art.html",{"gen":"True","img_path":result_pth, "name":"Abstract Art"})
    else:
        return render(request,"gans/abstract_art.html",{"gen":"False", "name":"Abstract Art"})



def simpson(request):
    if request.method == "POST":

        from .classes.simpson import save_samples
        result_pth = save_samples(4)
        
        
        return render(request,"gans/simpson.html",{"gen":"True","img_path":result_pth, "name":"Simpson"})
    else:
        return render(request,"gans/simpson.html",{"gen":"False", "name":"Simpson"})


def paint(request):
    if request.method == "POST":

        from .classes.paint import save_samples
        result_pth = save_samples(4)
        
        
        return render(request,"gans/paint.html",{"gen":"True","img_path":result_pth, "name":"Painter"})
    else:
        return render(request,"gans/paint.html",{"gen":"False", "name":"Painter"})


def flower(request):
    if request.method == "POST":

        from .classes.flower import save_samples
        result_pth = save_samples(4)
        
        
        return render(request,"gans/flower.html",{"gen":"True","img_path":result_pth, "name":"Flower"})
    else:
        return render(request,"gans/flower.html",{"gen":"False", "name":"Flower"})

def flower_imit(request):
    if request.method == "POST":

        from .classes.flower_imit import save_samples
        result_pth = save_samples(4)
        
        
        return render(request,"gans/flower_imit.html",{"gen":"True","img_path":result_pth, "name":"Flower"})
    else:
        return render(request,"gans/flower_imit.html",{"gen":"False", "name":"Flower"})

def cat(request):
    if request.method == "POST":

        from .classes.cat import generate
        result_pth = generate(4)        
        
        return render(request,"gans/cat.html",{"gen":"True","img_path":result_pth, "name":"Cat"})
    else:
        return render(request,"gans/cat.html",{"gen":"False", "name":"Cat"})

def anime(request):
    if request.method == "POST":

        from .classes.anime import save_samples
        result_pth = save_samples(4)        
        
        return render(request,"gans/anime.html",{"gen":"True","img_path":result_pth, "name":"Anime"})
    else:
        return render(request,"gans/anime.html",{"gen":"False", "name":"Anime"})

def human(request):
    if request.method == "POST":

        from .classes.human import generate
        result_pth = generate()        
        
        return render(request,"gans/human.html",{"gen":"True","img_path":result_pth, "name":"Human"})
    else:
        return render(request,"gans/human.html",{"gen":"False", "name":"Human"})